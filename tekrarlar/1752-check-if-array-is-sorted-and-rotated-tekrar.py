#isim = 1752-check-if-array-is-sorted-and-rotated
#etiket = Yeşil
#tekrar_cozum = 13.04.2026
#konu = Pivot Finding (Kırılma Noktası Bulma), Array Concatenation / Slicing (Dizi Birleştirme / Dilimleme)
# Sebep = yeni bir yolla denenecek. Slicing harici O(1) hafıza ile.


"""
1. Tekniğin Adı Nedir?Bu soruda kullandığın mantığın literatürdeki adı "Pivot Finding (Kırılma Noktası Bulma)" ve **"Array Concatenation / Slicing (Dizi Birleştirme / Dilimleme)"**dir.
2. Buradan Ne Öğrenmeliydin? (Kalıcı Zihin Notları)
Kural 1: Dairesel (Rotated) dizilerde her zaman tek bir kırılma (pivot) noktası vardır. Sıralı bir diziyi ne kadar kaydırırsan kaydır, büyük sayıdan küçük sayıya düşüş (yaşların düştüğü an) sadece ve sadece 1 kez yaşanır. Kırılmayı bul, oradan kes ve başa yapıştır.
Kural 2: Dilimleme (Slicing) Python'da çok güçlüdür. liste[:k] ve liste[k:] kullanarak bir diziyi ikiye bölmek ve ters sırayla toplamak (first + nums), karmaşık yer değiştirme (swap) algoritmalarından (amelelikten) kurtarır.
3. Bir Senior'ın "Hafıza" (Space Complexity) Dokunuşu:Senin kodun $O(N)$ hızında mükemmel çalışıyor. Hafızada yeni listeler (first, new_array) yarattığı için Space Complexity $O(N)$'dir.
Mülakatta sana "Bunu hiç yeni liste yaratmadan, ekstra hafıza kullanmadan ($O(1)$ Space) çözebilir misin?" diye sorarlarsa aklında şu ufak hile bulunsun:
Sıralı ve döndürülmüş bir dizide, elemanların bir sonraki elemandan büyük olduğu durum (kırılma anı) en fazla 1 kere olabilir. 
Sadece bir sayaç tutup bu düşüşleri sayarsın. Düşüş sayısı 1'den fazlaysa direkt False dönersin. (Son elemanla ilk elemanı da karşılaştırmayı unutmadan). Ama senin slicing yöntemin okunabilirlik açısından çok daha şıktır.






"""








class Solution:
    def check(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        early_e = True
        for k in range(1,len(nums)):
            if nums[k] >= nums[k-1]:
                continue
            else:
                first = nums[k:]
                nums = nums[:k]
                early_e = False
                break

        if early_e == True:
            return True
        new_array = first + nums
        for k in range(1,len(new_array)):
            if new_array[k] >= new_array[k-1]:
                continue
            else:
                return False
        return True
            