from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums = nums1[:m]
        
        i = j = k = 0
        while k < (m+n):
            if j < n:
                if i < m and nums[i] < nums2[j]:
                    nums1[k] = nums[i] 
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1
            else:
                nums1[k] = nums[i] 
                i += 1
            k += 1
        
        return nums1
# Time: O(m+n)
# Space: O(m)


    def merge_three_pointers(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1
        
        # add missing elements from nums2 IMPORTANT STEP
        nums1[:p2 + 1] = nums2[:p2 + 1]

        return nums1
            
# Time: O(m+n)
# Space: O(1)

solution = Solution()
print (solution.merge_three_pointers([1,2,3,0,0,0],3,[2,5,6],3))
