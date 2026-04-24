class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        result = 0
        for i,k in zip(heights,expected):
            if i != k:
                result += 1
        return result