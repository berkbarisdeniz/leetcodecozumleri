from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        r_hm = Counter(ransomNote)
        m_hm = Counter(magazine)
        return r_hm <= m_hm