class Solution:
    def addDigits(self, a: int) -> int:
        def helper(a):
            a = str(a)
            sumi = 0
            for i in a:
                sumi += int(i)
            return sumi
        
        while 10 <= a:
            a = helper(a)
        return a
