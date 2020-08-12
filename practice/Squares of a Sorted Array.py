class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        ret = list()
        for i in a:
            ret.append(i ** 2)
        return sorted(ret)
        
