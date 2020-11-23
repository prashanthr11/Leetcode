class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        l, maxi = [0] * (n + 1), 1
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        l[1] = 1
        
        if n % 2:
            for i in range(1, n // 2 + 1):
                if 2 * i + 1 <= n:
                    l[2 * i] = l[i]
                    l[2 * i + 1] = l[i] + l[i + 1]
                    maxi = max(maxi, l[2 * i + 1])
        else:
            for i in range(1, n // 2):
                if 2 * i + 1 <= n:
                    l[2 * i] = l[i]
                    l[2 * i + 1] = l[i] + l[i + 1]
                    maxi = max(maxi, l[2 * i + 1])
        return maxi

