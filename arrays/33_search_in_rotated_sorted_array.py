from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        # modified binary search
        while left<=right:
            mid = (right + left)//2
            
            if nums[mid] == target:
                return mid    
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
                    
        return -1

solution = Solution()
print (solution.search([4,5,6,7,0,1,2], 0))
# Time Complexity: O(log(n))
# Space Complexity: O(1)