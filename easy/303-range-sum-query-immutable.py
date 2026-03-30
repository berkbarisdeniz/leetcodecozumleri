class NumArray:

    def __init__(self, nums: list[int]):      
        self.prefix = []
        total = 0
        for k in range(len(nums)):
            total += nums[k]
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        else: return self.prefix[right] - self.prefix[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
