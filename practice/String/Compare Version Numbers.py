class Solution:
    def compareVersion(self, a: str, b: str) -> int:
        
        # Time: O(N) where N is the maximum length of version1 (a) and version2(b).
        # Space: O(N)
        
        a = a.split('.')
        b = b.split('.')
        
        if len(a) > len(b):
            b += [0] * (abs(len(a) - len(b)))
        if len(b) > len(a):
            a += [0] * (abs(len(a) - len(b)))
            
        for i in range(len(a)):
            if int(a[i]) > int(b[i]):
                return 1
            elif int(a[i]) < int(b[i]):
                return -1
            
        return 0
