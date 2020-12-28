class Solution:
    def numberOfSteps (self, n: int) -> int:
        
        # Time: O(N)
        # Space: O(1)
        
        cnt = 0
        
        while n:
            if n & 1:
                n ^= 1
            else:
                n = n >> 1
            cnt += 1
        
        return cnt
