class Solution:
    def lengthOfLIS(self, a: List[int]) -> int:
        ln = len(a)
        dp = [1] * ln
        
        for i in range(ln):
            for j in range(i):
                if a[j] < a[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)
