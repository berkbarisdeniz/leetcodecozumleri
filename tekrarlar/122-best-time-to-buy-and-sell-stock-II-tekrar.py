#isim = 122-best-time-to-buy-and-sell-stock-ii
#etiket = Yeşil
#tekrar_cozum = 13.04.2026
#konu = Array, Greedy, Zip Function



"""
Kural 1: Sınırsız al-sat izni olan durumlarda dip ve tepe noktalarını takip etmeye gerek yoktur. 
Sadece dünden bugüne olan pozitif farkları toplamak (Greedy yaklaşımı) maksimum kârı verir.

Kural 2: Bir listede ardışık elemanları karşılaştırmak 
için for i in range(1, len(liste)) yerine zip(liste, liste[1:]) kullanmak Python'da daha temiz bir okuma sağlar."""










class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = float("inf")
        max_profit = 0

        for price in prices:
            if low > price:
                low = price
            else:
                max_profit+= price-low
                low = price

        return max_profit
