class Solution:
    def totalMoney(self, n: int) -> int:
        
        # Time: O(N)
        # Space: O(1)
        
        ret, i = 0, 0
        cnt = 0
        
        while i < n:
            if i % 7 == 0:
                cnt += 1
                prev = cnt
            else:
                prev += 1
                
            ret += prev
            i += 1
                
        return ret
