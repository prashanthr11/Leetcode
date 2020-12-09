
from collections import Counter as di

class Solution:
    def numPairsDivisibleBy60(self, a: List[int]) -> int:
        a = [i % 60 for i in a]
        d = di(a)
        
        cnt = 0 
        for i in d:
            if i == 0 or i == 30:
                cnt += d[i] * (d[i] - 1) // 2
            elif d[i] > 0 and 60 - i in d:
                cnt += d[i] * d[60 - i]
                d[i] = 0

        return cnt
