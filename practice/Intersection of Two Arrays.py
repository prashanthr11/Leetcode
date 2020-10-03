class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        d, d1 = set(a), set(b)
        d2 = d.intersection(d1)
        return list(d2)
        
