class Solution:
    def decode(self, a: List[int], b: int) -> List[int]:
        
        # Time: O(N)
        # Space: O(1)
        
        ret = [b]
        
        for i in a:
            ret.append(ret[-1] ^ i)
            
        return ret
