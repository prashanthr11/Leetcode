from collections import defaultdict as dt

class Solution:
    def findDuplicate(self, a: List[int]) -> int:
        d = dt(int)
        for i in a:
            if d[i]:
                return i
            d[i] = 1
