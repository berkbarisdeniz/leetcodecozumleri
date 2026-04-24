#isim = 229-majority-element-ii
#etiket = Kırmızı
#tekrar_cozum = 31.03.2026
#konu = Boyer-Moore Voting Algorithm, Array, O(1) Space




"""
Kural 1: $n/k$ kuralı olan sorularda (burada $n/3$), en fazla $k-1$ tane aday (burada 2 aday) olabilir. 
$O(1)$ hafıza isteniyorsa Boyer-Moore gladyatör mantığı şarttır.

Kural 2: Boyer-Moore algoritması sana kesin kazananı vermez, sadece "potansiyel" en güçlü adayları verir. 
İşlem bittikten sonra bu adayların barajı gerçekten geçip geçmediğini orijinal veride 
tekrar sayarak kontrol etmek zorundasın (Aşama 2).


"""





















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