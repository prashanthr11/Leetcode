from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, a: List[List[int]]) -> List[int]:
        ret = []
        d = defaultdict(int)
        for i in a:
            d[i[1]] += 1
        for i in range(n):
            if d[i] == 0:
                ret.append(i)
        return ret
