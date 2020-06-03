from typing import List

class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        global visited
        visited = set()
        
        rows = len(board)
        cols = len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if (board[i][j] == word[0] 
                and self.searchWord(board , i, j ,0, word)):
                    return True
                    
        
        # if we have not returned True before, return False
        return False
    
    
    def searchWord(self, board, i, j, index, word):

        # here check for False: boundaries/ already visited / wrong letter
        if( i< 0 or j<0 or i>=len(board) or j>=len(board[0]) or(i,j) in visited 
           or word[index] != board[i][j]):
            return False
        
        # so index == word lenght -1 , so we found the word
        # because index starts from 0
        if index == len(word) - 1:
            return True
        
        visited.add((i,j))
        
        if(self.searchWord(board, i+1, j, index+1, word ) or
          self.searchWord(board, i, j+1, index+1, word) or
           self.searchWord(board, i-1, j, index+1, word) or
           self.searchWord(board, i, j-1, index+1, word)
          ):
            return True
        
             
        # so this i,j is not a solution, so remove from current visited
        visited.discard((i, j))
        return False


# Time O(N * 4**L) , where N - number of letters in board, L - len(word)
# SPACE : O(L + L) = O(L) , 1st L for visited set, 2nd L for recursion calls