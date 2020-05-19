from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0]) # n*logn
        
        result = []
        for interval in intervals: # n
            if not result or result[-1][1]<interval[0]:
                result += [interval]
            else:
                result[-1][1] = max(result[-1][1], interval[1])
                
        return result


# Time complexity: O(nlog(n))
# Sapce complexity: O(1) - не считаем резалт