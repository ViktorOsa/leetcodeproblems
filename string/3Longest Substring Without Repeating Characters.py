from typing import List


# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        max_counter = 0
        letters = {}
        start_window = 0
        
        for i in range(len(s)):
            # handle if we see same char again
            if s[i] in letters.keys() and letters[s[i]] >= start_window:
                max_counter = max(max_counter,i - start_window)
                start_window = letters[s[i]] + 1
             
            # here is a trick - we always add or overwrite prev char
            letters[s[i]] = i
            
        return max(max_counter, len(s) - start_window)
    
# Time: O(n), where n = len(s)
# Space: O(charset) so for ASCCI O(1)