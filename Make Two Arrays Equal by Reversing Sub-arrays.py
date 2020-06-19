class Solution:
    from collections import Counter
    def canBeEqual(self, a: List[int], b: List[int]) -> bool:
        s = Counter(a)
        s1 = Counter(b)
        return s == s1
        
