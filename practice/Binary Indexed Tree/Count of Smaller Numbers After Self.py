from bisect import bisect_left

class Solution:
    
    # Time: O(N Log N)
    # Space: O(N)
    
    def update(self, l):
        while l <= len(self.ft) - 1:
            self.ft[l] += 1
            l += l & -l
    
    def getsum(self, l):
        ret = 0
        while l > 0:
            ret += self.ft[l]
            l -= l & -l
            
        return ret
    
    def remove_negatives(self, a):    
        tmp = sorted(a)
        
        for i, j in enumerate(a):
            a[i] = bisect_left(tmp, j) + 1
            
        return a
        
    def countSmaller(self, a):
        a = self.remove_negatives(a)
        self.ft = [0] * (len(a) + 1)
        ret = list()
        
        for i in range(len(a) - 1, -1, -1):
            ret.append(self.getsum(a[i] - 1))
            self.update(a[i])
        
        return ret[::-1]
        
