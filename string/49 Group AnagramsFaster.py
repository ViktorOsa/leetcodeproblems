from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        for w in strs:
            chars = [0] * 26 
            for c in w:
                chars[ord(c) - ord('a')] += 1  
            
            d[tuple(chars)] = d.get(tuple(chars), []) + [w]
            
        return list(d.values())

# TIME: O(M * N) , M- len(strs), N len(words)
# SPACE O(M * N)