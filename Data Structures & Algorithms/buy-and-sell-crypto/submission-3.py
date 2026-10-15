class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_price = prices[0]

        for price in prices:
            current_profit = price - current_price
            if current_profit == 0:
                continue
            elif current_profit < 0:
                current_price = price
            
            max_profit = max(max_profit, current_profit)
        
        return max_profit