#isim = 41-first-missing-positive
#etiket = Kırmızı
#tekrar_cozum = 30.03.2026
#konu = Array, in-place, Cyclic Sort


"""
MÜHENDİSLİK NOTLARI: 41. First Missing Positive

Kavramsal Temel: 
Problem, değerler (sayılar) ile adreslerin (indeksler) birbiriyle doğrudan eşleşebildiği "Sıralı Adresleme" mantığına dayanır.
 Bir N uzunluğundaki dizide aranacak cevap her zaman [1, N+1] aralığındadır.

Elenen Alternatifler ve Trade-off'lar:
1. Normal Sıralama (O(N log N)): Diziyi sıralayıp eksik sayıyı bulmak en kolay yoldur ancak O(N) zaman kısıtını ihlal eder.
2. Hash Set Kullanmak (O(N) Zaman, O(N) Hafıza): Tüm sayıları bir Set'e atıp 1'den itibaren Set içinde arama yapmak hızı çözerdi. 
Ancak O(1) hafıza kuralı, dışarıdan herhangi bir veri yapısı açmamızı yasakladığı için bu da elendi.

Neden Cyclic Sort (In-place Swap)?
Mevcut dizinin kendisini bir Hash Map gibi kullanabilmemize olanak tanıdığı için. Ekstra RAM harcamadan, sadece veri bloklarının (öğrencilerin) yerini kendi içinde değiştirerek O(1) alan ve O(N) zaman kısıtlarının ikisini birden sağlayan tek mimaridir.

Kullanım Alanları:
- Belleğin (RAM) çok kısıtlı olduğu gömülü sistemlerde (embedded systems) veri düzenleme.
- 1'den N'e kadar sıralı olması beklenen veritabanı ID'lerinde kayıp olan (silinmiş veya bozuk) ID'leri ekstra bellek harcamadan tespit etme.
"""





class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        arr_len = len(nums)
        idx = 0
        while idx < arr_len:
            
            if nums[idx] > arr_len:
                idx += 1
            elif nums[idx] <= 0:
                idx += 1
            elif nums[idx] != nums[nums[idx]-1] :
                swap = nums[idx]-1 
                nums[swap], nums[idx] = nums[idx], nums[swap]
            else:
                idx += 1
        
        for idx in range(arr_len):
            if nums[idx] != idx+1 :
                return idx+1
        return nums[-1]+1





        