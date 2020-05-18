from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
 
        profit = 0      
        for i in range(1,len(prices)):
            if(prices[i] > prices[i-1]):
                profit  += (prices[i] - prices[i-1])
            
        return profit
    
    def maxProfit2(self, prices: List[int]) -> int:
        return sum([a - b for a, b in zip(prices[1:], prices) if a > b])

solution = Solution()
print (solution.maxProfit([7,1,5,3,6,4]))

# Time complexity: O(n)
# Sapce complexity: O(1)