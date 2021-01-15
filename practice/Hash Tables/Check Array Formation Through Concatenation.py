class Solution:
    def canFormArray(self, a: List[int], l: List[List[int]]) -> bool:
        
        # Time: O(N)
        # Space: O(N)
        
        d = dict()
        
        for i in l:
            d[i[0]] = i
            
        ret = list()
        
        for i in a:
            ret += d.get(i, [])
            
        return a == ret
