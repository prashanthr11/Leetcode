class Solution:
    def maxPower(self, s: str) -> int:
        maxi, cnt = 0, 1
        
        i, ln = 0, len(s)
        
        while i < ln:
            j = i + 1
            cnt = 1
            while j < ln and s[i] == s[j]:
                cnt += 1
                j += 1
            maxi = max(maxi, cnt)
            i += cnt
                    
        return max(maxi, cnt)
