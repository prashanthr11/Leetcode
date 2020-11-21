class Solution:
    def maxIncreaseKeepingSkyline(self, a: List[List[int]]) -> int:
        
        def helper(a):
            l = list()
            for i in range(len(a[0])):
                mini = -9984984653
                for j in range(len(a)):
                    mini = max(mini, a[j][i])
                l.append(mini)
            return l
        
        res = 0
        rowsMaxi = [max(i) for i in a]
        colsMaxi = helper(a)
        
        for i in range(len(a)):
            for j in range(len(a[0])):
                res += min(rowsMaxi[i], colsMaxi[j]) - a[i][j]
        return res
