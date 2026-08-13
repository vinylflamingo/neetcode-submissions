class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        lowest_buy = None

        for i, price in enumerate(prices):
            if i == 0: 
                lowest_buy = price

            if price < lowest_buy:
                lowest_buy = price

            max_profit = max(max_profit, (price - lowest_buy))
        
        return max_profit