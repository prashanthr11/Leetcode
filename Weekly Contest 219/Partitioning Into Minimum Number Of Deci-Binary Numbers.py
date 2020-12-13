class Solution:
    def minPartitions(self, n: str) -> int:
        maxi = int(n[0])
        for i in n[1:]:
            maxi = max(maxi, int(i))
        
        return maxi
