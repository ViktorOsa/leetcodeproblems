from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        size = len(nums)
        result = []
        for i in range(0, size-2):
            #if nums[i]> 0:
            #    break
            
            if i >0 and nums[i] == nums[i-1]:
                continue
                  
            s = i + 1
            e = size - 1
            while s < e:
                total = nums[s] + nums[e] + nums[i]
                if total == 0:
                    result.append ([nums[s], nums[e], nums[i]])
                    s += 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                    e -= 1
                    while s < e and nums[e] == nums[e+1]:
                        e -= 1
                elif total < 0:
                    s += 1
                else:
                    e -= 1
        return result


# Time: O(nlog(n) + n*n) = O(n*n)
# Space: O(1)