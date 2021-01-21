class Solution:
    def uniquePathsWithObstacles(self, a: List[List[int]]) -> int:
        
        # Time: O(MN)
        # Space: O(MN)
        
        dp = [[0] * (len(a[0]) + 1) for i in range(len(a) + 1)]
        dp[0][1] = 1
        
        for i in range(1, len(a) + 1):
            for j in range(1, len(a[0]) + 1):
                if a[i - 1][j - 1]:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            
        return dp[-1][-1]
                    
