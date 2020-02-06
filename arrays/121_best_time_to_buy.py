from typing import List

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

solution = Solution()
print (solution.maxProfit([7,1,5,3,6,4]))

# Time complexity: O(n)
# Sapce complexity: O(1)