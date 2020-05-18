from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0
        
        while(n>0):
            n = n & (n-1)
            counter += 1
            
        return counter