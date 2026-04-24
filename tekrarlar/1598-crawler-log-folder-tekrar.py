#isim = 1598-crawler-log-folder
#etiket = Yeşil
#tekrar_cozum = 31.03.2026
#konu = Stack, Simulation

"""
MÜHENDİSLİK NOTLARI: 1598. Crawler Log Folder

Kavramsal Temel: 
Geriye dönük işlemler (Undo/History) şablonu. Dizin (klasör) navigasyonu, 
doğası gereği bir LIFO (Son Giren İlk Çıkar) sistemidir. Yeni klasöre girildiğinde Push,
üst klasöre dönüldüğünde Pop işlemi yapılır.

Elenen Alternatifler ve Trade-off'lar (Kritik Mimari Fark):
1. Stack Listesi (Senin Çözümün): O(N) Zaman, O(N) Hafıza.
   Klasör isimlerini gerçekten bir listeye atar. Eğer soru bizden sadece 
   operasyon sayısını değil de "Şu an hangi dosya yolundayız? (Örn: /a/b/c)" 
   diye sorsaydı, bu yöntem ZORUNLUYDU.
   
2. Derinlik Sayacı (Integer Counter): O(N) Zaman, O(1) Hafıza.
   Soru sadece "ana klasöre kaç adım var?" diye sorduğu için aslında klasör 
   isimlerini hafızada tutmamıza gerek yoktur. Sadece bir `depth = 0` değişkeni 
   tutarak:
   - "../" geldiğinde: depth = max(0, depth - 1)
   - "./" geldiğinde: dokunma
   - "klasör" geldiğinde: depth += 1
   yaparak soruyu O(1) ekstra hafıza ile (In-place mantığıyla) çözebilirdik.

Neden Bu Çözüm?
Stack yapısının en temel fonksiyonlarını (Push, Pop, Empty Check) ve "Geri Al" 
mekanizmasını en şeffaf şekilde öğrettiği için.

Kullanım Alanları:
- İşletim sistemlerindeki dosya yolu (File Path) çözümleri.
- Tarayıcı geçmişi (Browser History - Back/Forward).
- Metin editörlerindeki Ctrl+Z (Undo) algoritmaları.
"""

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []

        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
                else:
                    pass
            

            elif log == "./":
                pass

            else:
                stack.append(log)
        return len(stack)