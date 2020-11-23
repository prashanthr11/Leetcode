class Solution:
    def numSpecial(self, a: List[List[int]]) -> int:
        def helper(a, j):
            l, i, ln = 0, 0, len(a)
            
            while i < ln:
                if a[i][j]:
                    l += 1 
                i += 1
                
            return l
            
            
        cnt = 0
        
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j]:
                    if a[i].count(1) == 1 and helper(a, j) == 1:
                        cnt += 1
            
        return cnt
