class Solution(object):
    def maxAscendingSum(self, nums):
        total = nums[0]
        big = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                total += nums[i]
                big = max(total,big)
            else:
                total = nums[i]
        return big