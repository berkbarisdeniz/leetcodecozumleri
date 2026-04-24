nums = [3,4,5,1,2]

class Solution:
    def check(self, nums: list[int]) -> bool:
        lenght=len(nums)
   
        for j in range(1,lenght):
            if nums[j] <= nums[j-1]:new_arr = nums[j:] + nums[:j]
        if new_arr:
            for j in range(lenght-1): 
                if new_arr[j] > new_arr[j+1]:return False

        return True

obj = Solution()

print(obj.check(nums))