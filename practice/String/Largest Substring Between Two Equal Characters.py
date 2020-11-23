from collections import defaultdict as dt

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s) == 1:
            return -1
        
        if len(s) == 2:
            return -1 if s[0] != s[1] else 0

        st = set()
        maxi = -1
        
        for i in range(len(s)):
            x = s.rfind(s[i])
            if i != x:
                maxi = max(maxi, x - i - 1)
                
        return maxi
