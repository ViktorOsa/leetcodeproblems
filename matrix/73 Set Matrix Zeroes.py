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

        set_i_j = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_i_j.add((i, j))
        
        while set_i_j:
            i, j = set_i_j.pop()
            self.setZeroesHelper(matrix, i, j, m, n)
        
               
    def setZeroesHelper(self, matrix, i, j, m, n):
        
        # set all values in a column to 0 
        for k in range(0,m):
            matrix[k][j] = 0
                
        # set all values in a raw to 0 
        for k in range(0,n):
            matrix[i][k] = 0 
        
            
