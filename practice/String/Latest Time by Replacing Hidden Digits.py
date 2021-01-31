class Solution:
    def maximumTime(self, s: str) -> str:
        
        # Time: O(N)
        # Space: O(N)
        
        s = list(map(str, s))
        i, ln = 0, len(s)
        while i < ln:
            if s[i] != '?' or s[i] == ':':
                i += 1
                continue
                
            if i == 0:
                if s[i + 1] == '?':
                    s[i] = '2'
                    s[i + 1] = '3'
                else:
                    if 0 <= int(s[i + 1]) <= 3:
                        s[i] = '2'
                    else:
                        s[i] = '1'
            elif i == 1:
                if s[i - 1] == '2':
                    s[i] = '3'
                elif s[i - 1] == '1':
                    s[i] = '9'
                else:
                    s[i] = '9'
            elif i == 3:
                if s[i + 1] == '?':
                    s[i], s[i + 1] = '5', '9'
                else:
                    s[i] = '5'
            elif i == 4:
                s[i] = '9'
            i += 1
            
        return ''.join(s)
