class Solution:
    def createSortedArray(self, a: List[int]) -> int:
        def update(n):
            nonlocal ft
            
            while n < len(ft):
                ft[n] += 1
                n += (n & -n)
                
        def getmini(n):
            nonlocal ft
            
            cnt = 0
            while n > 0:
                cnt += ft[n]
                n -= (n & -n)
                
            return cnt
        
        ft = [0] * (max(a) + 1)
        
        ret = 0
        for x, y in enumerate(a):
            ret += min(getmini(y - 1), x - getmini(y))
            update(y)
        
        return ret % (10 ** 9 + 7)
