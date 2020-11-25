class Solution:
    def arrangeWords(self, s: str) -> str:
        s = [i.lower() for i in s.split()]
        s.sort(key = lambda x:len(x))
        s[0] = s[0].title()
        return ' '.join(s)
        
