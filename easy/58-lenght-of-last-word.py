class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        result = 0
        for char in s:
            if char != " ":
                length += 1
                if char == s[-1]:
                    result = length
            else:
                if length != 0:
                    result = length
                length = 0
        
        return result

# ya da kısayoldan :  return len(s.strip().split(" ")[-1])

