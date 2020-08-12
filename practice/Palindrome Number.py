class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = list(map(str, str(x)))
        if x < 0:
            return False
        return s == s[::-1]
        
