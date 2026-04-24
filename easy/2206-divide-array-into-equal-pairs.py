from collections import Counter
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        hm = Counter(nums)
        return all(value % 2 == 0 for value in hm.values())