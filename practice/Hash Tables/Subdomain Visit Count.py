from collections import defaultdict as dt

class Solution:
    def subdomainVisits(self, a: List[str]) -> List[str]:
        d = dt(int)
        
        for i in a:
            tmp = i.split()
            d[tmp[1]] += int(tmp[0])
        
            tmp2 = tmp[1].replace('.', ' ').split()
            
            for i in range(1, len(tmp2)):
                y = '.'.join(tmp2[i:])
                d[y] += int(tmp[0])

        ret = list()
    
        for i in d:
            ret.append(str(d[i]) + ' ' + i)
            
        return ret
