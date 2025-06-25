def productExceptSelf(nums):
        left = []
        right = []
        result = []
        reverse_nums= nums[::-1]
        left.append(1)
        for idx in range(1,len(nums)):  
            left.append(left[idx-1]*nums[idx-1])
        right.append(1)
        for idx in range(1,len(nums)):  
            right.append(right[idx-1]*reverse_nums[idx-1])
        reverse_right = right[::-1]
        for idx in range(len(nums)):
            result.append(left[idx]*reverse_right[idx]) 
        return result