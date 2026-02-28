class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            temp_array = [0]*(i+1)
            temp_array[0] = 1
            temp_array[-1] = 1
            result.append(temp_array)
            if 2 <= i:
                for m in range(i-1):
                    result[i][m+1] = result[i-1][m]+result[i-1][m+1]
        return result
        