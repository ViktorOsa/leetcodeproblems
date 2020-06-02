from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if matrix == []:
            return []
        
        answer = []
        
        r = len(matrix)
        c = len(matrix[0])
        
        i_s, i_e = 0, r - 1
        j_s, j_e = 0, c - 1
        
        while len(answer) < r*c:
            
            # 1. moving in a row to the right
            i = i_s
            for j in range(j_s, j_e+1):
                answer.append(matrix[i][j])
            i_s += 1
            
            if len(answer) == r*c:
                break
            
            # 2. moving in a column down
            j = j_e
            for i in range(i_s, i_e + 1):
                answer.append(matrix[i][j])
            j_e -= 1
            
            if len(answer) == r*c:
                break
            
            # 3. moving in row to the left
            i = i_e
            for j in range(j_e, j_s - 1, -1):
                answer.append(matrix[i][j])
            i_e -= 1
            
            if len(answer) == r*c:
                break
            
            # 4. moving in a column up
            j = j_s
            for i in range(i_e, i_s - 1, -1):
                answer.append(matrix[i][j])
            j_s += 1
            
        
        return answer

# TIME : O(m * n)
# SPACE  O(1) or O(m*n) if count answer array


    ### SMART 
    def spiralOrderSMART(self, matrix):    #a while-loop version

        result = []

        while matrix:
            result.extend(matrix.pop(0))
            matrix = zip(*matrix)[::-1]    #rotate the remaining matrix counter-clockwise
            
        return result