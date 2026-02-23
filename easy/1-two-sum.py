class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for index,num in enumerate(nums):
            compliment = target-num
            if compliment in hashMap:
                return [hashMap[compliment],index]
            if num not in hashMap:
                hashMap[num] = index
                        
        
