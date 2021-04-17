class Solution:
    def countPoints(self, l: List[List[int]], q: List[List[int]]) -> List[int]:
        
        def dist(q, w, x, y):
            return ((q - x)**2) + ((w - y)**2)
        
        def solve(x, y, z):
            cnt = 0
            for q, w in l:
                tmp = dist(q, w, x, y)
                if tmp <= z**2:
                    cnt += 1
                    
            return cnt
                    
        
        ret = list()
        for x, y, z in q:
            ret.append(solve(x, y, z))
            
        return ret
