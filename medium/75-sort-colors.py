class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left = 0
        right = len(nums)-1
        j = 0

        while j <= right:
            if nums[j] == 2:
                nums[right],nums[j] = nums[j],nums[right]
                right -= 1
                

            elif nums[j] == 1:
                j += 1

            else:
                nums[left],nums[j] = nums[j],nums[left]
                left += 1
                j += 1
