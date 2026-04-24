#isim = 605-can-place-flowers
#etiket = Yeşil
#tekrar_cozum = 13.04.2026
#konu = Sliding Window, Frequency Array, Array Padding, Greedy Approach







            
        

"""
1. Tekniğin Adı Nedir?Bu tekniğin literatürdeki adı "Array Padding (Dizi Doldurma / Hayali Sıfır)" ve **"Greedy Approach (Açgözlü Yaklaşım)"**dır.
2. Buradan Ne Öğrenmeliydin? (Kalıcı Zihin Notları)
Kural 1: Uç noktalar (Edge Cases) can sıkıyorsa, evreni genişlet.Bir dizinin ilk ve son elemanını kontrol ederken IndexError yememek için bitmek bilmeyen if/else'ler yazmak yerine, dizinin başına ve sonuna sahte elemanlar ([0]) ekleyerek (Padding) bütün diziyi standartlaştırabilirsin.
Kural 2: Erken Çıkış (Early Exit / Short-Circuiting) sistemi kurtarır.Aradığın veya yerleştirmek istediğin hedef sayıya (n==0) ulaştığın an döngüyü anında return True ile kır. Bilgisayara gereksiz yere geri kalan 10.000 elemanı gezdirtme.
Kural 3: Kodda unutulan I/O işlemleri felakettir.Performans ölçümü yapılan yerlerde (LeetCode, Production ortamı) döngü içinde unutulan bir print(), $O(N)$ hızındaki mükemmel bir algoritmayı amele gibi yavaş gösterebilir.
3. Bu Teknik Başka Nerelerde Karşına Çıkar?
Oyun Tahtası / Izgara (Grid) Soruları: (Örn: Mayın Tarlası, Game of Life). Köşedeki bir hücrenin komşularını ararken hata almamak için tahtanın etrafını "Padding" ile görünmez duvarlarla çevirmek endüstri standardıdır.
Sınır Kontrolü Gerektiren Dizi Soruları: "Yan yana duran iki elemanın farkı..." diye başlayan ve ilk/son elemanlarda kuralın bozulduğu tüm senaryolarda hayat kurtarır.
Kural 4: Sabit Boyutlu Kayan Pencere (Fixed-Size Sliding Window) Algısı.Bir dizide "kendisinden önceki ve sonraki eleman" veya "yan yana duran 3 eleman" gibi lokal bloklar halinde kontrol yapıyorsak, bu aslında boyutu sabitlenmiş bir kayan penceredir. 
Pencereyi (k-1, k, k+1) her döngüde bir birim sağa kaydırarak lokal (bölgesel) kontrolleri $O(N)$ sürede ve en düşük maliyetle çözebiliriz.
"""








class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n==0 :
            return True
        
        flowerbed = [0] + flowerbed + [0]
        for idx in range(1,len(flowerbed)-1):
            if flowerbed[idx] == 0 and flowerbed[idx-1] == 0 and flowerbed[idx+1] == 0 : 
                flowerbed[idx] = 1
                n -= 1
                if n == 0:
                    return True
                
        return False