from typing import List

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        
        c = 1
        while i < j:
            if s[i] != s[j]:
                tmp1 = s[i+1:j+1]
                tmp2 = s[i:j]
                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
         
            i += 1
            j -= 1
            
        return True
        
# TIME: O(n) - because part with tmps we do once
# SPACE: O(1)