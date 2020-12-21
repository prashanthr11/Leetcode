class Solution:
    def wordPattern(self, a: str, b: str) -> bool:
        
        d = dict()
        j = 0
        b = b.split()
        
        if len(a) != len(b):
            return False
        
        for i in a:
            if i in d:
                if d[i] != b[j]:
                    return False
            d[i] = b[j]
            j += 1
        
        keys, values = set(d.keys()), set(d.values())
        return True if len(keys) == len(values) else False 
