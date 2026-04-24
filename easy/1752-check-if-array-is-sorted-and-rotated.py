class Solution:
    def check(self, nums: list[int]) -> bool:
        counter = 2
        step = len(nums)
        for i in range(1,step+1):
            if nums[i%step-1] <= nums[i%step]:
                continue
            else: 
                counter -= 1
                if counter == 0:
                    return False
        return True


        
#ögrendik