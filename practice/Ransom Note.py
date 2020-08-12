from collections import Counter as d

class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        c = d(a)
        c1 = d(b)
        return not len(c - c1)
