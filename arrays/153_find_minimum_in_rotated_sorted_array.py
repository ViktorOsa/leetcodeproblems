from typing import List

class Solution:
    
    def search(self, nums, start, end):
        if end - start <=1:
            return min(nums[start], nums[end])
        
        if nums[start] < nums[end]:
            return nums[start]
        
        mid = (end + start) // 2
        
        if nums[mid] > nums[start]:
            return self.search(nums, mid, end)
        else:
            return self.search(nums, start, mid)
    
    def findMin(self, nums: List[int]) -> int:    
        return self.search(nums, 0, len(nums)-1)

    def findMin_iterative(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]


solution = Solution()
print (solution.findMin([4,5,6,7,0,1,2]))

# Time complexity: O(log(n))
# Sapce complexity: O(1)