from itertools import permutations as perv

class Solution:
    def permute(self, a: List[int]) -> List[List[int]]:
        l = list(perv(a))
        l = [list(i) for i in l]
        return l
        
