from collections import Counter as di

class Solution:
    def uniqueOccurrences(self, a: List[int]) -> bool:
        d = di(a)
        return len(d.keys()) == len(set(d.values()))
        
