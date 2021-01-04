from collections import defaultdict as dt
from bisect import bisect_left

class Solution:
    def dailyTemperatures(self, a: List[int]) -> List[int]:
        
        # Time: O(N)
        # Space: O(N)
        
        ret = [0] * len(a)
        l = list()
        
        for i in range(len(a) - 1, -1, -1):
            while l and a[i] >= a[l[-1]]:
                l.pop()
                
            if len(l):
                ret[i] = l[-1] - i
            l.append(i)
        
        return ret
