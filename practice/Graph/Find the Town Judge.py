from collections import defaultdict as dt

class Solution:
    def findJudge(self, n: int, a: List[List[int]]) -> int:
        
        # Time: O(N) where N is length of the list
        # Space: O(N)
        
        indegree, outdegree = [True] *  (1 + n), [0] * (n + 1)
        
        for ind, out in a:
            indegree[ind] = False
            outdegree[out] += 1
            
        for i in range(1, n + 1):
            if indegree[i] and outdegree[i] == n - 1:
                return i
            
        return -1
