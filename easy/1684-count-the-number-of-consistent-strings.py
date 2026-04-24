class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)
        result = 0
        for word in words:
            check = True
            for j in word:
                if j not in allowed_set:
                    check = False
                    break
            if check:
                result += 1
        return result
                