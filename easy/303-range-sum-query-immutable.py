nums = [-2, 0, 3, -5, 2, -1]
right = 5
left = 2

prefix = []
total = 0
for k in range(len(nums)):
    print(k)
    total += nums[k]
    prefix.append(total)
    



print(prefix)
print(prefix[right]-prefix[left-1])



