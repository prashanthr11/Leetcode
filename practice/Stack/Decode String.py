class Solution:
    def decodeString(self, s: str) -> str:
        def endpoint(ind, s):
            cnt = 1
            for i in range(ind, len(s)):
                if s[i] == '[':
                    cnt += 1
                elif s[i] == ']':
                    cnt -= 1
                if cnt == 0:
                    return i
                    
        def getmultiplier(ind, s):
            tmp = ''
            for i in range(ind, -1, -1):
                if s[i].isdigit():
                    tmp += s[i]
                else:
                    return (int(tmp[::-1]), len(tmp))
            return (int(tmp[::-1]), len(tmp))
        
        while ']' in s:
            st = s.index('[')
            en = endpoint(st + 1, s)
            multiplies, ln = getmultiplier(st - 1, s)
            s = s[:st - ln] + multiplies * s[st + 1:en] + s[en + 1:]
        return s
