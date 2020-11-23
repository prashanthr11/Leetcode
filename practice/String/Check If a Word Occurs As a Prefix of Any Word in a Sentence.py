class Solution:
    def isPrefixOfWord(self, a: str, b: str) -> int:
        
        def helper(a, b):
            x, y = len(a), len(b)
            
            if x < y:
                return False
            for i in range(y):
                if a[i] != b[i]:
                    return False
            return True
        
        a = a.split()
        for i in range(len(a)):
            if helper(a[i], b):
                return i + 1
            
        return -1
