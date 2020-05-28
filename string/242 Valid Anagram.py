from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_dict = {}
        
        if len(s) != len(t):
            return False
        
        for c in s:
            letters_dict[c] = letters_dict.get(c,0) + 1
     
        for c in t:
            if letters_dict.get(c, 0) > 0:
                letters_dict[c] -= 1 
            else:
                return False
            
        
        return True

# TIME: O(n)
# SPACE: O(26 ~ O(1) for letters, and O(Unicode size) for unicode