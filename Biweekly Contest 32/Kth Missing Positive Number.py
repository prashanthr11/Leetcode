class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        ret = [i for i in range(1, 100001)]
        for i in a:
            ret.remove(i)
        return ret[k - 1]
