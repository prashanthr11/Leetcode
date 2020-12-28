class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        # Time: O(N)
        # Space: O(N)
        
        vowels = set('aeiou')
        cnt, ln = 0, len(s)
        
        window = list()
        
        for i in range(k):
            if s[i] in vowels:
                window.append(i)
                cnt += 1
        
        maxi = cnt
        i = k
            
        while i < ln:
            
            while window and window[0] <= i - k:
                window.pop(0)
                cnt -= 1
            
            if s[i] in vowels:
                window.append(i)
                cnt += 1
                maxi = max(maxi, cnt)
                
            i += 1
            
        return max(maxi, cnt)
