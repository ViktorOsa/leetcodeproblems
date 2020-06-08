from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
            
        return list(d.values())

# TIME O(M * NlogN) , where M - len(strs); NlogN sorting each string
# SPACE: O(M*N) - its full content that we save in dictionary