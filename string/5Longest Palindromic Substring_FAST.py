class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        answer = ""
        for i in range(len(s)):
            ii = self.expandFromMiddle(s, i, i)
            ij = self.expandFromMiddle(s, i, i+1)
            lenExpand = max(ii, ij)
            if lenExpand > len(answer):
                answer = s[i- int((lenExpand-1)/2):i+int(lenExpand/2)+1]
           
        return answer
    
    def expandFromMiddle(self, s, i, j):
        
        if ( i > j):
            return 0
        while (i >= 0 and j < len(s) and s[i] == s[j]):
            i -= 1
            j += 1
        
        return j - i - 1

# TIME: O(n*n)
# SPACE: O(1)