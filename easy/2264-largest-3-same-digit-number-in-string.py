class Solution:
    def largestGoodInteger(self, num: str) -> str:
        target = 0
        max_str = ""

        for j in range(1,len(num)):
            if num[j] == num[j-1]:
                target += 1
            
            else:
                target = 0
            
            if target == 2:
                current_str =num[j]*3
                
                if current_str > max_str:
                    max_str = current_str
                target = 0

        return max_str