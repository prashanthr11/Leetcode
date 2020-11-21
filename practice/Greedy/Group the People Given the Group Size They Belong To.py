from collections import defaultdict as dt

class Solution:
    def groupThePeople(self, l: List[int]) -> List[List[int]]:
        
        d = defaultdict(list)
        ret = list()
        for i in range(len(l)):
            d[l[i]].append(i)
            
        for k, v in d.items():
            while len(v) > k:
                tmp = list()
                for i in range(k):
                    tmp.append(v.pop())
                ret.append(tmp)
            ret.append(v)
        return ret
