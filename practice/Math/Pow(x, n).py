class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # Time: O(Log N)
        # Space: O(1)
        
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n == -1:
            return 1/x
        
        half = self.myPow(x, n // 2)
        
        if n & 1:
            return x * half * half
        
        return half * half
