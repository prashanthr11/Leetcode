class Solution:
    def kidsWithCandies(self, a: List[int], b: int) -> List[bool]:
        maxi = max(a)
        ret = list()
        a = [i + b for i in a]
        for i in a:
            if i >= maxi:
                ret.append(True)
            else:
                ret.append(False)
        return ret
