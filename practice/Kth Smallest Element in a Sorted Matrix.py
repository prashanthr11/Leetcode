class Solution:
    def kthSmallest(self, a: List[List[int]], b: int) -> int:
        l = list()
        for i in a:
            l += i
        l.sort()
        return l[b - 1]
