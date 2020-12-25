from collections import defaultdict as dt

class Solution:
    def findDiagonalOrder(self, a: List[List[int]]) -> List[int]:
        
        # Time: O(N * M) Where N and M are rows and columns respectively
        # Space: O(N * M)
        
        d = dt(list)
        
        for i in range(len(a)):
            for j in range(len(a[0])):
                d[i + j].append(a[i][j])
                
        ret = list()
        
        for k, v in d.items():
            if not k % 2:
                ret += v[::-1]
            else:
                ret += v
                
        return ret
        
