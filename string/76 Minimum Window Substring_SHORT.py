import collections

class Solution:
    def minWindow(self, s, t):
        # count each chars, that we are looking for
        # for example: {'a': 2, 'b':1} etc
        need = collections.Counter(t)
        
        # total number of missing chars
        missing =  len(t)
        
        # i - sliding window (left side)
        # I and J for answer
        i = I = J = 0
        
        # j - sliding window (right side)
        # c - char
        for j in range(len(s)):       
            if need[s[j]] > 0: # if we need this char - reduce missing counter
                missing -= 1
                
            need[s[j]] -= 1 # decrement counter for all chars
            
            if missing == 0: # if we found all needed chars
                # slide i to skip all chars not from t
                while i < j and need[s[i]] < 0: 
                    need[s[i]] += 1
                    i += 1
                if J == 0 or j - i + 1 <= J - I:
                    I, J = i, j+1
        return s[I:J]

# TIME: O (S + T): O(S) for main loop, O(T) for counter collections.Counter(t)
# SPACE: O(S + T) : because in worst case all chars from T are not in S