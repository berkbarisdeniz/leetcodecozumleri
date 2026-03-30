class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        arr_len = len(nums)
        idx = 0
        while idx < arr_len:
            
            if nums[idx] > arr_len:
                idx += 1
            elif nums[idx] <= 0:
                idx += 1
            elif nums[idx] != nums[nums[idx]-1] :
                swap = nums[idx]-1 
                nums[swap], nums[idx] = nums[idx], nums[swap]
            else:
                idx += 1
        
        for idx in range(arr_len):
            if nums[idx] != idx+1 :
                return idx+1
        return nums[-1]+1





        