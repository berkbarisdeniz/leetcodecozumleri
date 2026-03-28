class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cand_1 = None
        cand_2 = None
        counter_1 = 0
        counter_2 = 0
        result = []
        for num in nums:
            if num == cand_1 :
                counter_1 += 1
            elif num == cand_2 :
                counter_2 += 1
            elif counter_1 == 0:
                cand_1 = num
                counter_1 = 1
            elif counter_2 == 0:
                cand_2 = num
                counter_2 = 1
            else:
                counter_1 -= 1
                counter_2 -= 1

        target = len(nums) //3
        if nums.count(cand_1) > target:
            result.append(cand_1)
        if nums.count(cand_2) > target:
            result.append(cand_2)
        
        return result