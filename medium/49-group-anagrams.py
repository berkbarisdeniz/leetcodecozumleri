class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash = {}
        
        for word in strs:
            key = [0]*26
            for char in word:
                idx = ord(char) - ord('a')
                key[idx] += 1

            key = tuple(key)    
            if key in hash:
                hash[key].append(word)
            else:
                hash[key] = [word]

        return list(hash.values())