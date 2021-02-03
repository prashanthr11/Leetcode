class Solution:
    def decode(self, a: List[int]) -> List[int]:
        
        # Time: O(N)
        # Space: O(1)
        
        ret = 0
        n = len(a)
            
        for i in range(1, n + 2):
            ret ^= i
            
        for i in a[1::2]:
            ret ^= i
            
        l = [ret]
        for i in a:
            l.append(l[-1] ^ i)
            
        return l
