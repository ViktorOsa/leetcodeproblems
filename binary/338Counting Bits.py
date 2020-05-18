from typing import List

class Solution:
    def countBits_simple(self, num: int) -> List[int]:
        # we just do bit count for each interger 0 ... num
      
        bits = [0]        
        for i in range (1, num+1):
            bits.append(self.count_bits(i))
        
        return bits
        
    
    def count_bits(self, num):        
        counter = 0   
        while num >0:
            num = num & (num-1)
            counter += 1      
        return counter
    
    def countBits(self, num: int) -> List[int]:
        output = [0] * (num+1)
        
        if num==0:
            return output
        
        output[1] = 1
        
        for i in range (2, num+1):
            if i % 2 == 0:
                output[i] = output[i//2]
            else:
                output[i] = output[i-1] +1
    
        return output