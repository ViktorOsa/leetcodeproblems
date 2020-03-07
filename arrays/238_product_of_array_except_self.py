from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        nums_size = len(nums)
        
        L = [1] * nums_size
        R = [1] * nums_size
        ans = [0] * nums_size 
        
        for i in range(1, nums_size):
            L[i] = L[i-1] * nums[i-1]
            
        for i in range(nums_size-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
            
        for i in range(0, nums_size):
            ans[i]= L[i] * R[i]
            
        return ans

class Solution_2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length

        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]
        R = nums[-1]
        for i in range(length - 2, -1, -1):
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer

solution = Solution()
print (solution.productExceptSelf([1,2,3,4]))
# Time complexity: O(n)
# Sapce complexity: O(1)