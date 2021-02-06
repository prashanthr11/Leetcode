class Solution:
    def minimumLength(self, s: str) -> int:
        
        # Time: O(N)
        # Space: O(1)
        
        while len(s):
            if len(s) > 1 and s[0] == s[-1]:
                i = 1
                tmp = s[0]
                while i < len(s) and tmp == s[i]:
                    i += 1
                if i == len(s):
                    return 0
                j = len(s) - 1
                while j > i and s[j] == tmp:
                    j -= 1
                s = s[i:j + 1]
            else:
                break
            
        return len(s)
