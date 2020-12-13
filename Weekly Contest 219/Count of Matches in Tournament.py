from math import ceil as cl

class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        cnt = 0
        while n != 1:
            cnt += n // 2
            
            if n % 2:
                n = cl(n / 2)
            else:
                n = n // 2
            
        return cnt
