from collections import Counter as di

class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        d1 = di(b)
        ret = list()
        for i in a:
            if d1[i]:
                d1[i] -= 1
                ret.append(i)
        return ret
