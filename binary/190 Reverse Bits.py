from typing import List

class Solution:
    def reverseBits(self, n: int) -> int:
        res, mask = 0, 1
        for _ in range(32):
            # here ws my mistake
            res = res<< 1 ## ! free place for new incomer
            res = res|( n & mask ) # calculate new icomer and add it 
            n =  n >> 1 # shift value
        return res