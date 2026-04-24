#isim = 3442-maximum-difference-between-even-and-odd-frequency-i
#etiket = Yeşil
#tekrar_cozum = 13.04.2026
#konu = Hash Table, Counting, State Tracking






"""
Kural 1: Frekans (sayma) işlemi duyduğunda her zaman kılıcın collections.Counter olmalı. 
Bu, arka planda C ile yazılmış çok optimize bir Hash Table'dır ve manuel sözlük (dict) kurmaktan çok daha hızlıdır.

Kural 2: Listede aynı anda hem en büyük hem en küçük değeri arıyorsan, 
listeyi parçalamak veya yerleşik fonksiyonlarla birden fazla kez taramak yerine, 
tıpkı borsa sorusundaki gibi başlangıç değerleri (0 ve float('inf')) atayıp tek bir for döngüsünde işi bitir.

"""












from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        odd_max = 0
        even_min = float("inf")
        for num in list(Counter(s).values()):
            if num % 2 == 0 and num < even_min:
                even_min = num
            elif num % 2 == 1 and num > odd_max:
                odd_max = num

        return odd_max-even_min
        
