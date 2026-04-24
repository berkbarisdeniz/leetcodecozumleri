from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hm = Counter(nums)
        total = 0
        for value in hm.values():
           total += (value * (value-1))/2
        return int(total)

