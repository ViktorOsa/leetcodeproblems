import collections
from typing import List

class Solution:
    def leastInterval_one(self, tasks: List[str], n: int) -> int:
        task_counter = collections.Counter(tasks)
        
        most_common_task = task_counter.most_common(1)[0][1]
        
        # to use just counter i calculate idles also for most common
        # elelemnt (: n+1). Later i substruct it
        extra_idles = (most_common_task - 1) * ( n+1 )
        
        # now we substruct our tasks from extra_idles
        for k,v in task_counter.items():
            extra_idles -= min(v, most_common_task - 1)
        
        # extra_idles can not be negative
        extra_idles = max(extra_idles, 0)
     
        return extra_idles + len(tasks)
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # dictionary to calculate occurrence 
        tsk_cnt = {}
        
        # iterate over keys
        for i in tasks:
            if i in tsk_cnt:
                tsk_cnt[i] += 1
            else:
                tsk_cnt[i] = 1
                
        lst = sorted (tsk_cnt.values(), reverse=True)
        
        # calculate how many we have most occuring tasks
        mst = lst[0]
        cnt = 0
        for i in lst:
            if i == mst:
                cnt += 1
            else:
                break
        
        return max(len(tasks), (mst -1) * (n + 1) + cnt)

# Time: O(n)
# Space: O(1)