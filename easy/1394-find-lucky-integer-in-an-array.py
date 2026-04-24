class Solution:
    def findLucky(self, arr: list[int]) -> int:
        hm = {}
        for num in arr:
            hm[num] = hm.get(num,0)+1
        result = [key for key,value in hm.items() if key == value]
        return max(result) if result else -1
                