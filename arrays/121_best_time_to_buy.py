class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) == 0):
            return 0
        
        max_profit = 0
        min_value = prices[0]
        for price in prices:
            if price <= min_value:
                min_value = price
            else:
                curr_profit = price - min_value
                if curr_profit > max_profit:
                    max_profit = curr_profit
        
        return max_profit