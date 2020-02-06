from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        if len(nums) == 1:
            return False
        set_nums = set()
        for num in nums:
            if num in set_nums:
                return True
            set_nums.add(num)
        
        return False

solution = Solution()
print (solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
# Time complexity: O(n)
# Sapce complexity: O(n)