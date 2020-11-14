from collections import Counter as di

class Solution:
    def isIsomorphic(self, a: str, b: str) -> bool:
        return len(di(a)) == len(di(b))
