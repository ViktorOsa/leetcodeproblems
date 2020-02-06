from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for index, value in enumerate(nums):       
            complement = target - value
            if complement in complements.keys():
                return [index, complements[complement]]
            else:
                complements[value] = index

solution = Solution()
print (solution.twoSum([2, 7, 11, 15], 18))
# Time Complexity: O(n)
# Space Complexity: O(n)