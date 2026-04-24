class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0]
        self.total = 0
        for num in nums:
            self.total += num
            self.prefix.append(self.total)
        print(self.prefix)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]



obj1 = NumArray([1,2,3,4,5,9,0,78])
print(obj1.sumRange(2,4))

        
