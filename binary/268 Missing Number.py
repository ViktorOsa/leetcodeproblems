from typing import List

class Solution:
    def missingNumber_sorting(self, nums: List[int]) -> int:
        nums.sort()
        
        if nums[0] != 0:
            return 0
        elif nums[-1] != (len(nums)):
            return len(nums)
        else:
            for i in range(1,len(nums)):
                if nums[i] != i:
                    return i
    
    def missingNumber_hash(self, nums: List[int]) -> int:
        hs = set (nums)
        upper_range = len (nums) + 1
        
        for num in range(upper_range):
            if num not in hs:
                return num
            
            
    def missingNumber_xor(self, nums: List[int]) -> int:
        # using XOR , 2^2 = 0 !
        
        max_num = len (nums)
        
        for i, v in enumerate(nums):
            max_num^=i^v
        
        return max_num
    
    
    def missingNumber(self, nums: List[int]) -> int:
        
        # using gaus sum formula E0_n = (n *(n+1)) /2
        
        num = len (nums)
        expected_sum = num * (num +1) //2
        
        return expected_sum - sum(nums)