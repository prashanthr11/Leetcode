class Solution:
    def nextGreaterElement(self, a: List[int], b: List[int]) -> List[int]:
        ret = list()
        def fnd(x):
            ind = b.index(x)
            for i in b[ind + 1:]:
                if x < i:
                    return i
            return -1
        for i in a:
            ret.append(fnd(i))
        return ret
