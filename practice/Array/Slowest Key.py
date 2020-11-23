class Solution:
    def slowestKey(self, a: List[int], s: str) -> str:
        diff = [a[0]]
        maxi, ln = a[0], len(a)        
        
        for i in range(1, ln):
            diff.append(a[i] - a[i - 1])
            maxi = max(maxi, diff[-1])
            
        ind = diff.index(maxi)
        ret = s[ind]
        
        for i in range(ind + 1, ln):
            if diff[i] == maxi and not ret > s[i]:
                ret = s[i]
                
        return ret
        
