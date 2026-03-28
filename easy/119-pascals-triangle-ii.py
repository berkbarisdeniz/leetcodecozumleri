class Solution:
    def getRow(self,rowIndex: int) -> list[int]:
            array = [1]
            for _ in range(rowIndex):
                array.append(1)
                for k in range(len(array)-2,0,-1):
                    array[k] = array[k] + array[k-1]
            return array
            