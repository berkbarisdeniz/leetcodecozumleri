class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        new = set()
        result=[]
        for num in grid:
            for subnum in num:
                if subnum not in new:
                    new.add(subnum)
                else:
                    result.append(subnum)
        for k in range(1,len(grid)**2+1):
            if k in new:
                continue
            else:
                result.append(k)
        return result