from typing import List

class Solution:
    def moveZeroes_hard_to_get(self, nums):
        p1 = p2 = 0
        
        for p2 in range(len(nums)):
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                if p2 != p1:
                    nums[p2] = 0
                p1 += 1
            p2 += 1

        return nums

    def moveZeroes(self, nums):

        non_zero_ptr = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_ptr] = nums[i]
                non_zero_ptr += 1
        
        while non_zero_ptr < len (nums):
            nums[non_zero_ptr] = 0
            non_zero_ptr += 1
        
        return nums

solution = Solution()
print (solution.moveZeroes([0,1,0,3,12]))

# Time complexity: O(n)
# Sapce complexity: O(1)