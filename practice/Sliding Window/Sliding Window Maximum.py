from collections import deque as dq

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        ret, maxi = list(), dq()
        
        for i in range(k):
            while len(maxi) and a[maxi[-1]] < a[i]:
                maxi.pop()
                
            maxi.append(i)
        ret.append(a[maxi[0]])
        
        for i in range(k, len(a)):
            
            while len(maxi) and maxi[0] <= i - k:
                maxi.popleft()
            
            while len(maxi) and a[maxi[-1]] < a[i]:
                maxi.pop()
                
            maxi.append(i)
            ret.append(a[maxi[0]])
            
        return ret
