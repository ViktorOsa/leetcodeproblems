from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        i = m - 1
        j = 0
        
        while j <= n - 1:
            if i > 0:
                if not self.checkDiagonal(matrix, i, j, m, n):
                    return False
                i -= 1
            else:
                if not self.checkDiagonal(matrix, i, j, m, n):
                    return False
                j += 1
        
        return True
                
    def checkDiagonal(self, matrix, i, j, m , n):
        while i < m - 1 and j < n-1:
            if matrix[i+1][j+1] != matrix[i][j]:
                return False
            i += 1
            j += 1
        
        return True

# TIME: O(n*m)
# SPACE: O(1)