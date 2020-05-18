from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) -1
        water = 0
        while l<r:
            water = max (water, (r-l)*min(height[r], height[l]))
            
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        
        return water

# Time: O(n)
# Space: O(1)