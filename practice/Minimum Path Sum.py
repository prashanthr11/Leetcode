class Solution:
    def minPathSum(self, a: List[List[int]]) -> int:
        row, col = len(a), len(a[0])
        ret = [[0 for i in range(col)] for i in range(row)]
        
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    ret[i][j] = a[i][j]
                elif i == 0:
                    ret[i][j] = ret[i][j - 1] + a[i][j]
                elif j == 0:
                    ret[i][j] = ret[i - 1][j] + a[i][j]
                else:
                    ret[i][j] = min(ret[i - 1][j] + a[i][j], ret[i][j - 1] + a[i][j])
                
        return ret[-1][-1]
