from collections import Counter as di

class Solution:
    
    # Time: O(N)
    # Space: O(N)
    
    def countBalls(self, a: int, b: int) -> int:
        def solve(i):
            ret = 0
            while i:
                ret += i % 10
                i //= 10
                
            return ret
        
        d = di()
        for i in range(a, b + 1):
            d[solve(i)] += 1
            
        return max(d.values())
