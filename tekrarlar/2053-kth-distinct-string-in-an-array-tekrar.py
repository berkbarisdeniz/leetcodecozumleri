#isim = 2053-kth-distinct-string-in-an-array
#etiket = Yeşil
#tekrar_cozum = 23.04.2026
#konu = Hash Table, Counting, O(1) Space Optimization







""""
Kural 1: Benzersiz (Distinct) veya "sadece 1 kere geçen" gibi ifadeler duyduğunda her zaman Counter kullan. 
Modern Python'da Counter ilk eklenme sırasını korur.
Kural 2: Eğer senden sadece $K$. eleman isteniyorsa, tüm geçerli elemanları bir listeye doldurup sonra indeksle çağırmak ameleliktir. 
Geri sayım sayacı (k -= 1) kullanarak bulduğun an return ile çıkış yap ($O(1)$ ekstra hafıza).

"""





from collections import Counter

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        freq = Counter(arr)
        for key,value in freq.items():
            if value == 1:
                k -= 1 
                if k == 0:
                    return key
        return ""
