class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        
        for i in range(len(s)):
            counter += self.expandFromMiddle(i, i, s)
            counter += self.expandFromMiddle(i, i+1, s)
        
        return counter
    
    
    def expandFromMiddle(self, i, j, string):
        
        localCounter = 0
        
        
        while (i>=0 and j<len(string) and string[i]==string[j]):
            localCounter += 1
            i-=1
            j+=1
        
        
        return localCounter

# TIME: O(n^2)
# SPACE: O(1)