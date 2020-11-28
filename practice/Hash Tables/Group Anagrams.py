from collections import defaultdict as dt

class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        ret = dt(list)
        for i in a:
            ret[tuple(sorted(i))].append(i)
        return ret.values()
