class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ''
        MOD = int(1e9) + 7
        for i in range(1, n + 1):
            res += bin(i)[2:]
        ret = int(res, 2) 

        return ret % MOD
