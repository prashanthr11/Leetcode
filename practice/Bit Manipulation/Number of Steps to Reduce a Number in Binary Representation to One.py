class Solution:
    def numSteps(self, s: str) -> int:
        
        # Time: O(N)
        # Space: O(1)
        
        cnt = 0
        n = int(s, 2)
        
        while n != 1:
            n = n + 1 if n & 1 else n >> 1
            cnt += 1
            
        return cnt
