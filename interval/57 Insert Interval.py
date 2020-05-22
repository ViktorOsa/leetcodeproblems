from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            
        result = []
        
        for interval in intervals: 
            if newInterval == None or interval[1] < newInterval[0]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = None
                result.append(interval) # IMPORTANT
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        
        if newInterval is not None:
            result.append(newInterval)
                  
        return result

# TIME: O(n)
# SPACE O(n)