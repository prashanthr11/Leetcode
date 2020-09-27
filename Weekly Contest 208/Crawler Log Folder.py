class Solution:
    def minOperations(self, a: List[str]) -> int:
        cnt = 0
        for i in a:
            if '../' == i:
                if cnt > 0:
                    cnt -= 1
                else:
                    cnt = 0
            else:
                if i[-2] != '.':
                    cnt += 1
        if cnt < 0:
            cnt = 0
        return cnt
        
