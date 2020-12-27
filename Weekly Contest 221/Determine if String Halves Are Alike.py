class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        # Time: O(N) where N is the length of the string.
        # Space: O(1)
        
        vowels = 'aeiou'
        s = s.lower()
        
        n = len(s) // 2
        a, b = 0, 0
        
        for i in range(len(s) // 2):
            if s[i] in vowels:
                a += 1
            if s[-i - 1] in vowels:
                b += 1
        
        return a == b
