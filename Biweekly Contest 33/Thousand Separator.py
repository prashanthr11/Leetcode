class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = reversed(str(n))
        ret = ""
        cnt = 0
        for i in ans:
            if cnt == 3:
                ret += "."
                cnt = 0
            ret += i
            cnt += 1
        return ''.join(reversed(ret))
        
