class Solution:
    def restoreMatrix(self, row: List[int], col: List[int]) -> List[List[int]]:
        r, c = len(row), len(col)
        
        ret = [[0 for i in range(c)] for j in range(r)]
        
        for i in range(r):
            for j in range(c):
                ret[i][j] = min(row[i], col[j])
                row[i] -= ret[i][j]
                col[j] -= ret[i][j]
        
        return ret
