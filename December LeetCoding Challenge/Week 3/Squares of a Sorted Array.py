class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        a = [i ** 2 for i in a]
        return sorted(a)
        
