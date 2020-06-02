from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix == [[]]:
            return
        
        m = len(matrix) # number of raws
        n = len(matrix[0]) # number of columns
        
        set_raws = set()
        set_cols = set()
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_raws.add(i)
                    set_cols.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in set_raws or j in set_cols:
                    matrix[i][j] = 0 

# TIME O(m*n)
# SPACE ( m + n)
        
            

        
            
