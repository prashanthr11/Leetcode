from collections import Counter as di

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = di(s)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
        
