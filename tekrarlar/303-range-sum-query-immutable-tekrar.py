#isim = 303-range-sum-query-immutable
#etiket = Yeşil
#tekrar_cozum = 23.04.2026
#konu = Array Padding, Prefix Sum








"""
1. Tekniğin Adı Nedir?Bu tekniğin literatürdeki adı "Prefix Sum" (Ön Ek Toplamı / Kümülatif Toplam) ve hata önleme mekanizması olarak da "Array Padding" (Hayali Sıfır) kombinasyonudur.
2. Buradan Ne Öğrenmeliydin? (Kalıcı Zihin Notları)
Kural 1: "Aralık Toplamı" (Range Sum) sorusu duyarsan, Prefix Sum kılıcını çek. Kullanıcı sürekli "3. gün ile 7. gün arasındaki satışların toplamı ne?" diye soruyorsa, her seferinde o aralığı döngüyle toplamak (amelelik - $O(N)$) sistemi çökertir. 
Bunun yerine en başta kümülatif toplamların olduğu bir harita çıkarıp (mühendislik), her soruyu sadece tek bir çıkarma işlemiyle ($O(1)$ hızında) cevaplarsın.
Kural 2: Baştaki hayali sıfır [0], "if/else" cehenneminden kurtarır.Eğer dizinin en başından (0. indeksten) başlayan bir toplam istenirse, formülde sol tarafı çıkarırken negatif indekse veya "Acaba 0'dan mı başlıyor?" diye kontrol eden bir if bloğuna düşmemek için prefix listesini [0] ile başlatırız.
3. Bu Teknik Başka Nerelerde Karşına Çıkar?
2D Range Sum Query (Görüntü İşleme / Matrisler): Sadece tek boyutlu listelerde değil, iki boyutlu haritalarda veya resimlerde "Şu koordinatlar arasındaki piksellerin toplamı nedir?" gibi sorularda 2D Prefix Sum kullanılır.
Finansal veya İstatistiksel Dashboardlar: Veritabanındaki "Son 30 günlük ciro", "Geçen haftanın ziyaretçi sayısı" gibi sürekli aralık sorgulanan metriklerin anında hesaplanması gereken backend mimarilerinde sıklıkla uygulanır.
Continuous Subarray Sum: "Bir dizide, toplamı k'nın katı olan ardışık bir alt dizi var mı?" tarzı klasik algoritma sorularında.


"""




class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0]
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
