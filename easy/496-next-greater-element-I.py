nums1 = [4,1,2]
nums2 = [1,3,4,2]
stack = []
hm = {}
result = []


for num in nums2:
    if not stack:
        stack.append(num)
    else:
        if stack[-1] > num :
            stack.append(num)
        else:
            while stack and num > stack[-1]:
                hm[stack[-1]]=num
                stack.pop()

            stack.append(num)
for num in stack:
    hm[num] = -1


for num in nums1:
    result.append(hm[num])

print(result)


