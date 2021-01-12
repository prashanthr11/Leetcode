from collections import defaultdict as dt

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        # Time: O(N) where N is the range of numbers from lo to hi [lo, hi].
        # Space: O(N)
        
        def solve(n):
            nonlocal d
            if d[n]:
                return d[n]
             
            if n % 2:
                d[n] = 1 + solve(n * 3 + 1)
            else:
                d[n] = 1 + solve(n // 2)
            return d[n]
        
        k -= 1
        d = dt(int)
        d[1] = 1
        ret = list()
        
        for i in range(lo, hi + 1):
            d[i] = solve(i)
            ret.append((d[i] - 1, i))
        
        ret.sort()
        
        return ret[k][1]
