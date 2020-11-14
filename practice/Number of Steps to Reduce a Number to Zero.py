class Solution:
    def numberOfSteps (self, a: int) -> int:
        cnt = 0
        while a > 0:
            cnt += 1
            if not a % 2:
                a = a // 2
            else:
                a -= 1
        return cnt
        
