class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        track=0
        hm = {}
        for word in arr:
            hm[word] = hm.get(word,0)+1
        for num in hm:
            if hm[num] == 1:
                track += 1
            if track == k:
                return num
        return ""
