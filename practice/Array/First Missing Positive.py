from collections import Counter as di

class Solution:
    def firstMissingPositive(self, a: List[int]) -> int:
        
        # Constant Space
        a.append(0)
        ln = len(a)
        
        for i in range(ln):
            if a[i] < 0 or a[i] >= ln:
                a[i] = 0
                
                
        for i in range(ln):
            a[a[i] % ln] += ln
            
        for i in range(ln):
            if not  a[i] // ln:
                return i
                
        return ln
        
        '''
        from collections import Counter as di
        
        d = di(a)
        i, ln = 1, len(a)
        
        while i <= ln:
            if not d[i]:
                return i
            i += 1
            
        return i
        '''
