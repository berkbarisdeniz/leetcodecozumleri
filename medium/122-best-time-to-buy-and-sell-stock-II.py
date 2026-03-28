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
