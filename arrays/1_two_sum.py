class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for index, value in enumerate(nums):       
            complement = target - value
            if complement in complements.keys():
                return [index, complements[complement]]
            else:
                complements[value] = index