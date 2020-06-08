class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        answer = ""
        for i in range(len(s)): # O(n)
            for j in range(len(s), i, -1): # O(n)
                if j-i < len(answer):
                    break
                
                if s[i:j] == s[i:j][::-1]: # O(n)
                    answer = s[i:j]
        
        return answer
                    
# TIME O(n^3)
# SPACE: O(n) for answer