#isim = 121-best-time-to-buy-and-sell-stock
#etiket = Yeşil
#tekrar_cozum = 27.03.2026
#konu = Array, Dynamic Programming (State Machine), Greedy








"""
Kural 1: Geleceği tahmin etmen gereken finansal/zaman çizelgesi sorularında her zaman "O anki en kötü durumu" (low) ve "O anki en iyi sonucu" (max_profit) cebinde taşıyarak ilerle.

Kural 2: İlk değeri atamakta zorlanıyorsan (örneğin ilk elemanı low yapmak döngüyü bozuyorsa), her zaman float('inf') veya float('-inf') kullan. İlk iterasyonda zaten ezip geçecektir.

"""












class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = float('inf')
        max_profit = 0

        for price in prices:
            
            if low >= price:
                low = price
            
            else:
                profit = price - low
                
                if profit > max_profit:
                    max_profit = profit

        return max_profit