class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        out = []
        new= set(nums)
        for k in range(1,len(nums)+1):
            if k in new:
                continue
            else:
                out.append(k)
        return out

        




"""in-place negation"""
nums = []
for i,num in enumerate(nums):
    if nums[abs(num)-1]>0:
        (nums[abs(num)-1]) *= -1
print(nums)
"""sonrası pozitif indexler eksik olanlar."""