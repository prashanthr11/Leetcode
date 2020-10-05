class Solution:
    def numWaterBottles(self, a: int, b: int) -> int:
        cnt = 0
        while a > 0:
            if a >= b:
                a -= b
                cnt += b
            else:
                cnt += a
                return cnt
            a += 1
        return cnt
        
