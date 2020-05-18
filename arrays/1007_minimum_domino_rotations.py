from typing import List

class Solution:    
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        rotations = -1
        # check rotations for list A
        rotations = self.check(A, B, A[0])
        
        # check rotations for list B
        if (rotations == -1 and A[0] != B[0]):    
            rotations = self.check(B, A, B[0])
        
        return rotations
    
    def check(self, list_one, list_two, num):
        
        rot_a = rot_b = 0
        for i in range(len(list_one)):
            if (list_one[i] != num and list_two[i] != num):
                return -1
            elif(list_one[i] != num and list_two[i] == num):
                rot_a += 1         
            elif(list_two[i] != num and list_one[i] == num):
                rot_b += 1
    
        return min(rot_a, rot_b)

# Time complexity: O(n)
# Sapce complexity: O(1)

    def minDominoRotations_slow(self, A: List[int], B: List[int]) -> int:
        
        # define which number is most often in an array
        nums = [0]*7
        for i in range(len(A)):
            nums[A[i]]+=1
            nums[B[i]]+=1
        
        # if we have most frequent more or equal array lenth save it
        most_freq_num = -1
        for i in range(len(nums)):
            if nums[i] >= len(A):
                most_freq_num = i
                break
        
        if most_freq_num == -1:
            return -1
        
        
        # check rotations needed
        rot_a = rot_b = 0
        for i in range (len(A)):
            if (A[i] != most_freq_num and B[i] != most_freq_num):
                return -1
            else: 
                if(A[i] != most_freq_num):
                    rot_a += 1
            
                if(B[i] != most_freq_num):
                    rot_b += 1
        
        return min(rot_a, rot_b)
            
        
solution = Solution()
print (solution.minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2]))

            
                