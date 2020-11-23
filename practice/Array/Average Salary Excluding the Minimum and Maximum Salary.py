class Solution:
    def average(self, a: List[int]) -> float:
        
        sumi, ln = 0, len(a)
        mini, maxi = 966798764434, 0
        
        for i in range(ln):
            sumi += a[i]
            mini = min(mini, a[i])
            maxi = max(maxi, a[i])
        
        return (sumi - mini - maxi) / (ln - 2)
        
        '''
        return (sum(a) - min(a) - max(a)) / len(a[:-2])
        '''
