class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = arr[-1]
        leng=len(arr)
        for index,num in enumerate(arr[-2::-1]):
            arr[leng-index-2] = right_max
            if right_max < num :
                right_max = num
        arr[-1] = -1
        return arr

   