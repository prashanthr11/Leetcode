class Solution:
    def sortArrayByParity(self, a: List[int]) -> List[int]:
        l = list()
        o = []
        e = []
        for i in a:
            if i % 2:
                o.append(i)
            else:
                e.append(i)
        l = e + o
        return l
