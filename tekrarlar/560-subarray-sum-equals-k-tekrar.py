#isim = 560-subarray-sum-equals-k
#etiket = Kırmızı
#tekrar_cozum = 01.04.2026
#konu = Array, Hash Table, Prefix Sum

"""
MÜHENDİSLİK NOTLARI: 560. Subarray Sum Equals K

Kavramsal Temel:
Problem "Tersine Mühendislik" ve "Ön-Toplam (Prefix Sum)" mantığına dayanır.
Normal denklem: Gecmis_Toplam + Hedef_Alt_Dizi(k) = Su_Anki_Toplam
Bizim aradığımız (Sorgu): Aranan_Gecmis_Toplam = Su_Anki_Toplam - k
Eğer bu aranan geçmiş toplamı daha önce gördüysek, o noktadan şu anki 
noktaya kadar olan kısmın toplamı kesinlikle k'dır.

Elenen Alternatifler ve Trade-off'lar:
1. İç İçe Döngüler (Brute Force - O(N²)): Her eleman için geriye/ileriye dönük 
   toplam hesaplamak veri seti büyüdüğünde sistemi kilitler.
2. Geçmişi Listede Tutmak (O(N²)): Dünkü ilk denemede olduğu gibi, aranan sayıyı 
   bir liste (Array) içinde 'in' veya '.count()' ile aramak, her adımda listeyi 
   baştan sona tarattığı için döngü içinde döngü yaratır ve Time Limit (TLE) yedirir.

Neden Hash Map (Sözlük) Mimarisi?
Sözlük yapısı, arama (lookup) ve ekleme (insertion) işlemlerini O(1) hızında yapar. 
Ayrıca negatif sayılar yüzünden aynı toplamı birden fazla kez görebileceğimiz için, 
sadece varlığını (True/False) değil, frekansını (kaç kere gördüğümüzü) tutmak zorundayız. 
Başlangıçtaki {0: 1} değeri, "dizinin en başından başlayan geçerli alt dizileri" 
kaçırmamak için konulan hayati bir köprüdür.

Kullanım Alanları:
- Finansal analizlerde belirli bir net kar/zarar (k) elde edilen zaman 
  aralıklarını (periyotları) hızlıca tespit etme.
- Sinyal işleme ve sensör verilerinde belirli bir eşik değere ulaşan 
  dalga boylarını yakalama.
"""

"""
MÜHENDİSLİK NOTLARI: 560. Subarray Sum Equals K

Kategori: Prefix Sum + Hash Map (Two Sum Mantığı)
Karmaşıklık: O(N) Zaman | O(N) Hafıza

Çekirdek Mantık (Tersine Mühendislik):
Normal beklenti: Gecmis_Toplam + Aradaki_Alt_Dizi = Su_Anki_Toplam
Algoritma mantığı: Aranan_Gecmis_Toplam = Su_Anki_Toplam - k

Eğer (Su_Anki_Toplam - k) değerini geçmişte gördüysek, o eski noktadan 
bulunduğumuz noktaya kadar olan kısmın toplamı kesinlikle k'dır.

Kritik Mimari Kararlar:
1. Veri Yapısı Seçimi (Liste vs Hash Map): 
   Listede arama yapmak O(N) sürede gerçekleşir ve iç içe döngü yaratır.
   Hash Map (sözlük) ile arama O(1)'dir. Ayrıca negatif sayılar toplamı 
   dalgalandıracağı için sadece sayının varlığını değil, "frekansını" 
   (kaç kez görüldüğünü) tutmak zorundayız. (Başlangıç durumu: {0: 1})
   
2. İşlem Sırası Tuzağı (Kendi Kendini Sayma):
   Döngü içinde HER ZAMAN önce geçmiş kontrol edilmeli (if check in hash), 
   sonra o anki toplam deftere yazılmalıdır (hash[total_sum] += 1). 
   Eğer önce kayıt yapılıp sonra kontrol edilirse, kod k=0 senaryolarında 
   kendi güncel değerini geçmişte bulmuş gibi davranıp sahte artış yapar.
"""
























class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        total_sum = 0
        result = 0
        hash = {0:1}
        for idx,num in enumerate(nums):
            total_sum += num 
            check = total_sum - k
            if check in hash :
                result += hash[check]
            hash[total_sum] = hash.get(total_sum,0)+1
        return result




