class Solution:
    def minSubArrayLen(self, s: int, a: List[int]) -> int:
        
        # Time: O(N) Where N is the length of the given list
        # Space: O(N) 
        
        mini = 123456789
        
        l = list()
        
        i, sumi, ln, j = 0, 0, len(a), 0
        
        while i < ln:
            
            while j < ln and sumi < s:
                l.append(a[j])
                sumi += a[j]
                j += 1
            
            while len(l) and sumi >= s:
                mini = min(mini, len(l))
                sumi -= l[0]
                l.pop(0)
            
            i = j
            
        # if sum(l) >= s:
        #     mini = min(mini, len(l))
        
        return mini if mini != 123456789 else 0
