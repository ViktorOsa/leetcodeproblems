from typing import List
import collections

class Solution:
    
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
# Time complexity: O(n)
# Sapce complexity: O(1)
    
    def majorityElement_one(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
# Time complexity: O(n)
# Sapce complexity: O(n)
    
    def majorityElement_two(self, nums: List[int]) -> int:
        
        counter = len(nums)//2 + 1
        
        bucket = {}
        
        for num in nums:
            if num in bucket:
                bucket[num] +=1
            else:
                bucket[num] = 1
            
            if bucket[num] >= counter:
                return num
# Time complexity: O(n)
# Sapce complexity: O(n)

solution = Solution()
print (solution.majorityElement([2,2,1,1,1,2,2]))