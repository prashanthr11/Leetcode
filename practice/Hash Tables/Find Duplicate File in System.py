class Solution:
    def findDuplicate(self, a: List[str]) -> List[List[str]]:
        l = list()
        d = collections.defaultdict(list)
        
        for i in a:
            tmp = i.split()
            root = tmp[0]
            for i in tmp[1:]:
                l.append(root + '/' + i)
                
        for i in l:
            tmp = i.split('(')
            d[tmp[1][:-1]].append(tmp[0])
            
        ret = list()
        for k, v in d.items():
            if len(v) > 1:
                ret.append(v)
                
        return ret
