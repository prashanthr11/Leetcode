from collections import Counter as di

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return di(s) == di(t)
        
