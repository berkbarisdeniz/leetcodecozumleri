class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for k in range(len(nums)-1):
            if (nums[k]+nums[k+1])%2 == 0: 
                return False
        return True
        