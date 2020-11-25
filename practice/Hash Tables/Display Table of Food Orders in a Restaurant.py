from collections import defaultdict as dt

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        st = set()
        for i in orders:
            st.add(i[2])
        
        foods = sorted(list(st))
        tables = dt(lambda: [0] * len(foods))
        
        for order in orders:
            tables[order[1]][foods.index(order[2])] += 1
        
        ret = [["Table"] + foods]
        
        for k, v in sorted(tables.items(), key = lambda x:int(x[0])):
            v = [str(i) for i in v]
            ret.append([k] + v)
            
        return ret
