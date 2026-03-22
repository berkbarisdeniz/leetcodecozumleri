class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc_streak = 1
        dec_streak = 1
        big = 1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i] :
                inc_streak += 1
                dec_streak = 1
            elif nums[i-1] > nums[i] :
                dec_streak += 1
                inc_streak = 1
            else:
                inc_streak = 1
                dec_streak = 1
            big = max(big,inc_streak,dec_streak)
        return big
        