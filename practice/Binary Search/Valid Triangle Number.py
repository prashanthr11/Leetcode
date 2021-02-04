class Solution:
    def triangleNumber(self, a: List[int]) -> int:
        
        # Time: O(N ^ 2)
        # Space: O(1)
        
        cnt = 0
        a.sort()
        n = len(a)
        
        for i in range(n - 2):
            k = i + 2
            if a[i] == 0:
                continue
            for j in range(i + 1, n):
                while k < n and a[i] + a[j] > a[k]:
                    k += 1
                cnt += k - j - 1
            
        return cnt
