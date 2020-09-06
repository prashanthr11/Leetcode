from string import ascii_lowercase as lc

class Solution:
    def modifyString(self, s: str) -> str:
        ls = list(map(str, s))
        l = lc
        
        if len(ls) == 1:
            if ls[0] == '?':
                return 'a'
            else:
                return s
        
        if ls[0] == '?':
            for i in l:
                if ls[1] != i:
                    ls[0] = i
                    break
                    
        if ls[-1] == '?':
            for i in l:
                if ls[-2] != i:
                    ls[-1] = i
                    break
        
        for i in range(1, len(ls) - 1):
            if ls[i] == '?':
                for j in range(len(l)):
                    if ls[i-1] != l[j] and ls[i+1] != l[j]:
                        ls[i] = l[j]
                        break
                        
        return ''.join(ls)
