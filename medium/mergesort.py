nums = [38, 27,2,43]

def mergeSort(arr):
    if len(arr) == 1:       #1- base case
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]       #2- parçalama

    sortedLeft = mergeSort(left)    
    sortedRight = mergeSort(right)  #3- recursive kısım
    print("sayısı.")
    return merge(sortedLeft,sortedRight) #4- bir üst fonksiyona geri dönüş yapacak return
                                    # fonksiyonu en iç base case hariç tüm fonksiyonları bitiren return
def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result
print(mergeSort(nums))