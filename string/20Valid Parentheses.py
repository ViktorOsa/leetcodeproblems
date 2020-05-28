from typing import List

class Solution:
    def isValid(self, s: str) -> bool:

        b_dict = {")":"(", "}":"{", "]":"["}
          
        
        starts = b_dict.values() # to avoid O(n) in a loop
        # tho in python 3 .keys() is O(1) !
        
        char_stack = [] # newest at the end
        for c in s:
            if c in starts:
                char_stack.append(c)
            elif char_stack and char_stack[-1] == b_dict.get(c, ""):
                char_stack.pop()
            else:
                return False
            
        
        return len(char_stack) == 0

# TIME: O (n)
# SPACE: O(n)