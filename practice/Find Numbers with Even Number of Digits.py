class Solution:
    def findNumbers(self, a: List[int]) -> int:
        l = [len(str(i)) for i in a]
        ret = 0
        for i in l:
            if not i % 2:
                ret += 1
        return ret
        
        
