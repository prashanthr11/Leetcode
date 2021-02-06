from collections import Counter as di

class Solution:
    def sumOfUnique(self, a: List[int]) -> int:
        
        # Time: O(N)
        # Space: O(N)
        
        d = di(a)
        ret = 0
        
        for i in d:
            if d[i] == 1:
                ret += i
                
        return ret
