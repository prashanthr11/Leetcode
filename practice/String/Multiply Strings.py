class Solution:
    def multiply(self, a: str, b: str) -> str:
        x, y = 0, 0
        ln1, ln2 = len(a), len(b)
        
        for i in range(ln1):
            tmp = ord(a[i]) - ord('0')
            x += tmp * (10 ** (ln1 - i - 1))
            
        for i in range(ln2):
            tmp = ord(b[i]) - ord('0')
            y += tmp * (10 ** (ln2 - i - 1))
            
        return str(x * y)
