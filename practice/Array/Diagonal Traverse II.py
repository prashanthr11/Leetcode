from collections import defaultdict as dt

class Solution:
    def findDiagonalOrder(self, a: List[List[int]]) -> List[int]:
        
        # Time: O(R * C) Where R and C are length of the row and columns of the matrix respectively
        # Space: O(R * C)
        
        d = dt(list)
        ret = list()
        
        for i in range(len(a)):
            for j in range(len(a[i])):
                d[i + j].append(a[i][j])
                
        for k, v in d.items():
            ret += v[::-1]
            
        return ret
