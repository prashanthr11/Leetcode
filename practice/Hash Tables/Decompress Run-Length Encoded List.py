class Solution:
    def decompressRLElist(self, a: List[int]) -> List[int]:
        
        def rep(a, b):
            l = list()
            for i in range(b):
                l.append(a)
            return l
        
        i, l = 0, list()
        while i < len(a):
            l += rep(a[i + 1], a[i])
            i += 2
        return l
        
