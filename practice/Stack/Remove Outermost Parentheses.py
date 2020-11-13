class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ret, cnt, start = '', 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
            if cnt == 0:
                ret += s[1 + start:i]
                start = i + 1
        return ret
                
            
