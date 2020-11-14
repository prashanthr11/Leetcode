class Solution:
    def maxWidthOfVerticalArea(self, a: List[List[int]]) -> int:
        a = [i[0] for i in a]
        a.sort()
        ret = -987
        for i in range(1, len(a)):
            ret = max(ret, a[i] - a[i - 1])
        return ret
