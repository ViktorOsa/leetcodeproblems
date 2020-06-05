from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        ## Important to understand the solution
        # The longest substring will always contain the most 
        # frequent character, in that way, 
        # we do not need to change the max_counter.
        letters_counter = {}
        
        max_counter = 0 # to count most frequent letter
        max_len = 0
        start_window = 0
        
        for i in range(len(s)):
            # 1. add letter to letters_counter dict 
            # and update max_counter
            if s[i] not in letters_counter:
                letters_counter[s[i]] = 0
            letters_counter[s[i]] += 1
            max_counter = max(letters_counter[s[i]], max_counter)
            
            
            # 2. check condition for sliding window
            if (i - start_window + 1 - max_counter > k):
                ## DO NOT FORGET TO REDUCE frequency !!!! 
                letters_counter[s[start_window]] -= 1
                # we slide
                start_window += 1
            
            # 3. update max_len
            max_len = max(max_len, i - start_window + 1)
              
        return max_len

# TIME O(n)
# SPACE O(26) = O(1) 