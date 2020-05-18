from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        if (target > nums[-1] and target < nums[0]):
            return -1
        
        if(target >= nums[0] and target <= nums[-1]):
            return self.binary_search( nums, 0, len(nums)-1, target)
            
        min_index = self.search_min_index(nums, 0, len(nums)-1)
        if (target > nums[min_index]  and target >= nums[0]):
            return self.binary_search( nums, 0, min_index, target)
        else:
            return self.binary_search( nums, min_index, len(nums)-1, target)
        
    def search_min_index(self, nums, l, r):        
        if r-l <=1:
            if nums[l]< nums[r]:
                return l
            else:
                return r
             
        mid = (r+l)//2
        
        if (nums[mid] > nums[l]):
            return self.search_min_index(nums, mid, r)
        else:
            return self.search_min_index(nums, l, mid)
    
    def binary_search(self, nums, left_index, right_index, target):
        
        if (right_index - left_index <=1):
            if nums[left_index] == target:
                return left_index
            elif nums[right_index] == target:
                return right_index
            else:
                return -1

        mid = (left_index + right_index)//2 
        if(nums[mid] == target):
            return mid
        elif(nums[mid] > target):
            return self.binary_search(nums, left_index, mid, target)
        else:
            return self.binary_search(nums, mid, right_index, target)


solution = Solution()
print (solution.search([4,5,6,7,0,1,2], 0))
# Time Complexity: O(log(n))
# Space Complexity: O(1)