from collections import Counter as di

class Solution:
    def getHint(self, a: str, b: str) -> str:
        d1, d2 = di(), di()
        bulls, cows, ln = 0, 0, len(a)
        
        for i in range(ln):
            if a[i] == b[i]:
                bulls += 1
            else:
                d1[a[i]] += 1
                d2[b[i]] += 1
                
        for i in d2:
            cows += min(d1[i], d2[i])
            
        return "{0}A{1}B".format(bulls, cows)
