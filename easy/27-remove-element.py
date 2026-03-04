class Solution(object):
    def removeElement(self, nums, val):
        for idx,num in enumerate(nums) :
            if num == val :
                nums.remove(nums[idx])
                nums.append(val)
        k = 0
        if nums:
            for num in nums:
                if val != num:
                    k += 1
                else:
                    return k
        else:
            return k
        


"""
kaldırıp eklemek tehlikeli index sırasını bozar büyük ihtimal bunda çalıştı ama şöyle yapabilirdik
direkt nums[a] = nums[b] gibi atama şeklinde yapabilirdik ama ilk aklıma bu geldi ve çalıştı dokunmadım.    
"""