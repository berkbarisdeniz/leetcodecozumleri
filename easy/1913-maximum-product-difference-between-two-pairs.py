class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        low1 = low2 = 10**4 +1
        high1 = high2 = 0

        for num in nums:
            if num > high1:
                high2 = high1
                high1 = num
            elif num > high2:
                high2 = num
            
            if num < low1:
                low2 = low1
                low1 = num
            elif num < low2:
                low2 = num

        return (high1*high2)-(low1*low2)