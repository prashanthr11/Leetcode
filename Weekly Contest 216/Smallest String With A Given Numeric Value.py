from string import ascii_lowercase as lc

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        tmp = lc
        ret = ['a'] * n
        k -= n
        i = n - 1

        while k > 25:
            ret[i] = 'z'
            k -= 25
            i -= 1

        if k:
            ret[i] = tmp[k]
        return ''.join(ret)
            
