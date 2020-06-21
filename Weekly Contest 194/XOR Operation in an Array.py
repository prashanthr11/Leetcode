class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l = list()
        for i in range(n):
            l.append(start + 2 * i)
        sumi = 0
        for i in l:
            sumi ^= i
        return sumi
        