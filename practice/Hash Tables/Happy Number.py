from collections import defaultdict as dt

class Solution:
    def isHappy(self, n: int) -> bool:
        d = dt(int)
        def helper(a):
            sumi = 0
            while a > 9:
                sumi += (a % 10) ** 2
                a //= 10
            sumi += a ** 2
            
            return sumi
        
        while n > 1:
            d[n] = 1
            n = helper(n)
            if d[n]:
                return False
        if n == 1:
            return True
        return False
        
