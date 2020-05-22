from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
           
        if len(intervals) < 2:
            return 0
        
        intervals.sort(key = lambda x:x[1])
        
        end = intervals[0][1]      
        to_remove = 0     
        for interval in intervals[1:]:
            
            if interval[0] < end:
                to_remove += 1
            else:
                end = interval[1]

               
       
        return to_remove

# TIME O(nlogn)
# SPACE O(1)