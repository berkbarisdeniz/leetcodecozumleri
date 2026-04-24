#isim = 2486-append-characters-to-string-to-make-subsequence
#etiket = Sarı
#tekrar_cozum = 27.03.2026  
#konu = Two Pointers (While Loop Habit), String Matching, Greedy
#sebep = while döngüsü kullanarak







"""
1. Tekniğin Adı Nedir?Bu mantığın literatürdeki adı "Two Pointers" (İki İşaretçi) ve eşleşmeyi bulduğu an affetmeden aldığı için **"Greedy Approach" (Açgözlü Yaklaşım)**dır.
2. Buradan Ne Öğrenmeliydin? (Kalıcı Zihin Notları)
Kural 1: Sıra bozulmaması gereken iki dizi varsa, İki İşaretçi şarttır. İç içe iki tane for döngüsü kurmak ($O(N^2)$) yerine, iki diziyi de kendi indeksleriyle (biri for döngüsü k, diğeri dışarıdaki arr_idx) aynı anda paralel olarak yürütürsen sistem $O(N)$ hızında akar.
Kural 2: Dilimleme (Slicing) RAM düşmanıdır. Geriye kalan elemanların kendisi değil de sadece sayısı (uzunluğu) soruluyorsa, len(t[index:]) ile yeni dizi yaratmak yerine her zaman len(t) - index matematiğini kullan.











"""





class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        arr_idx = 0
        for k in range(len(s)):
            if t[arr_idx] == s[k]:
                arr_idx += 1
                if arr_idx == len(t):
                    return 0
                
        return(len(t)-arr_idx)

        