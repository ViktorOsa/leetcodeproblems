from typing import List
class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) -1
        
        while (p1<p2):
            sum_numbers =  numbers[p1] + numbers[p2]
            if sum_numbers == target:
                return [p1+1, p2+1]
            elif sum_numbers > target:
                p2 -= 1

#Time O(n)
#Space O(1)

solution = Solution()
print (solution.twoSum([2, 7, 11, 15], 9))