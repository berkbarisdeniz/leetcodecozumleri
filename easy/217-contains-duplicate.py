class Solution(object):
    def containsDuplicate(self, nums):
        result = set()
        for k in nums:
            if k not in result:
                result.add(k)
            else:
                return True
        return False