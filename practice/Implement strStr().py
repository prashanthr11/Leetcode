class Solution:
    def strStr(self, a: str, b: str) -> int:
        try:
            return a.index(b)
        except ValueError:
            return -1
        
