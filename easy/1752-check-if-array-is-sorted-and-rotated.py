class Solution:
    def check(self, nums: list[int]) -> bool:
        sp_idx=0
        new1=[]
        new2=[]
        if sorted(nums) == nums:
            return True 
        for k in range(len(nums)-1):
            if nums[k+1] < nums[k]:
                sp_idx = k
        for k in range (len(nums)):
            if k <= sp_idx:
                new1.append(nums[k])
            else:
                new2.append(nums[k])
        sortednew = new2 + new1
        return sortednew == sorted(nums)
    
    #nums[i] > nums[(i + 1) % N] tek satır circular düşünürsen. Öğrenecez