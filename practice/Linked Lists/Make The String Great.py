class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            if len(s) <= 1:
                return s
            if len(s) == 2:
                if abs(ord(s[0]) - ord(s[1])) == 32:
                    return ''
            t = ''
            i = 1
            while i < len(s):
                if abs(ord(s[i]) - ord(s[i-1])) == 32:
                    t += s[i+1:]
                    break
                else:
                    t += s[i - 1]
                i += 1
            if i == len(s):
                if abs(ord(s[-2]) - ord(s[-1])) != 32:
                    t += s[-1]
            if len(s) == len(t):
                return s
            s = t

        
