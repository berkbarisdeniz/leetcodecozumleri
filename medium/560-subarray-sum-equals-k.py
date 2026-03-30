class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        total_sum = 0
        result = 0
        hash = {0:1}
        for num in nums:
            total_sum += num 
            check = total_sum - k
            if check in hash :
                result += hash[check]
            hash[total_sum] = hash.get(total_sum,0)+1
        return result




