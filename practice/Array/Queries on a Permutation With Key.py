from collections import deque as dq
from itertools import islice

class Solution:
    
    # Time: O(N * 2)
    # Space: O(N)
    
    def processQueries(self, a: List[int], b: int) -> List[int]:
        ret = list()
        l = dq([i for i in range(1, b + 1)])
        
        for i in a:
            tmp = l.index(i)
            ret.append(tmp)
            l = dq(islice(l, 0, tmp)) + dq(islice(l, 1 + tmp, b))
            # l.remove(i)
            l.appendleft(i)
        
        return ret
            
