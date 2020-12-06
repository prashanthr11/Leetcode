from collections import Counter as di

class Solution:
    def maxOperations(self, a: List[int], k: int) -> int:
        d = di(a)
        cnt = 0
        
        for i in a:
            if d[i] > 0:
                if k - i == i:
                    if d[i] > 1:
                        d[i] -= 2
                        cnt += 1
                else:
                    if d[k - i] > 0:
                        d[k - i] -= 1
                        d[i] -= 1
                        cnt += 1
        return cnt
