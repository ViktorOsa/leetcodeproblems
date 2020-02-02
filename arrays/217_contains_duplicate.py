class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        if len(nums) == 1:
            return False
        set_nums = set()
        for num in nums:
            if num in set_nums:
                return True
            else:
                set_nums.add(num)
        
        return False