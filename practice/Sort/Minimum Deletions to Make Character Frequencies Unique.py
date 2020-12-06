from collections import Counter as di
from collections import defaultdict as dt

class Solution:
    def minDeletions(self, s: str) -> int:
        d = di(s)
        x = dt(int)
        cnt = 0
        
        for i in d:
            if not x[d[i]]:
                x[d[i]] = 1
            else:
                tmp = d[i]
                while x[tmp] and tmp > 0:
                    tmp -= 1
                    cnt += 1
                if tmp:
                    x[tmp] = 1
        return cnt
