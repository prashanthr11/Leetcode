class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        # Time: O(N)
        # Space: O(N)
        
        opened = list()
        place = dict()
        
        for i in range(len(s)):
            if s[i] == '(':
                opened.append(i)
                
            if s[i] == ')':
                tmp = opened.pop()
                place[i] = tmp
                place[tmp] = i
                
        ret = ''
        
        i, d = 0, 1
        
        while i < len(s):
            if s[i] in '()':
                i = place[i]
                d = -d
            else:
                ret += s[i]
            
            i += d
        
        return ret
