class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        # Time: O(N)
        # Space: O(1)
        
        tmp = 0
        
        for i in s:
            if i.isdigit():
                tmp *= int(i)
            else:
                tmp += 1
                
        for i in range(len(s) - 1, -1, -1):
            k = k % tmp
            if k == 0 and s[i].isalpha():
                return s[i]
            
            if s[i].isdigit():
                tmp //= int(s[i])
            else:
                tmp -= 1
