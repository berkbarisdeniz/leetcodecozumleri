"""
çoğunluk olanlar: min %34 olanlar. yani en fazla 2 tane olabilir -> %68. 3. bir çoğul olamaz [n//3] için.
haliyle bunun özel bir algoritması var.
"""

nums = [2,1,1,3,1,4,5,6]
cand_1 = None
cand_2 = None
count_1 = 0
count_2 = 0
result = []

for num in nums:
    if num == cand_1:
        count_1 += 1
    
    elif num == cand_2 :
        count_2 += 1

    elif count_1 == 0:
        cand_1 = num
        count_1 = 1

    elif count_2 == 0:
        cand_2 = num
        count_2 = 1

    else:
        count_1 -= 1
        count_2 -= 1

target = len(nums) // 3
if nums.count(cand_1) > target:
    result.append(cand_1)
if nums.count(cand_2) > target:
    result.append(cand_2)
print(result)