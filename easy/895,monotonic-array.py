class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        trend = 0
        for k in range(len(nums)-1):
            if nums[k] == nums[k+1]:
                continue
            elif nums[k]>nums[k+1]:
                if trend == -1:
                    return False
                trend = 1
            else:
                if trend == 1:
                    return False
                trend = -1
        return True
"""
increasing = True
        decreasing = True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
            if nums[i] < nums[i + 1]:
                decreasing = False
                
        return increasing or decreasing

two flag deniyormuş.


Diyelim ki bir kullanıcının girdiği şifreyi kontrol ediyorsun. Şartlar: En az 1 büyük harf, 1 küçük harf ve 1 rakam içermeli. 
Bunu döngülerle veya karmaşık Regex (düzenli ifadeler) ile yapmak yerine bayrakları dikersin:

has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper(): has_upper = True
    elif char.islower(): has_lower = True
    elif char.isdigit(): has_digit = True

return has_upper and has_lower and has_digit
"""





