class Solution(object):
    def isIsomorphic(self, s, t):
        seen = {}
        seen_values = set()
        for idx,char in enumerate(s):
            if char not in seen:
                if t[idx] in seen_values:
                    return False
                seen[char] = t[idx]
                seen_values.add(t[idx])
                
            else:
                if t[idx] != seen[char]:
                    return False
        return True