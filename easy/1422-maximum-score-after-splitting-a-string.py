class Solution:
    def maxScore(self, s: str) -> int:
        right = s.count("1",1)
        left = 1 if s[0] == "0" else 0
        result= right+left
        for k in range(1,len(s)-1):
            if s[k] == "1":
                right -= 1
            else:
                left += 1
            result = max(result, left+right)
                
        return result