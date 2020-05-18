from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        cur_max = res_min = res_max = nums[0]
        
        for i in range(1, len(nums)):
            res_min_before = res_min
            res_min = min(nums[i], res_min*nums[i], res_max*nums[i])
            
            res_max = max(nums[i], res_min_before*nums[i], res_max*nums[i])
            cur_max = max(cur_max, res_max)
            
        return cur_max

solution = Solution()
print (solution.maxProduct([2,3,-2,4]))

# Time complexity: O(n)
# Sapce complexity: O(1)