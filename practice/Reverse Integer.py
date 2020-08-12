class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31:
            return 0
        l = list(map(str, str(x)))
        s = ""
        if x < 0:
            for i in range(len(l) - 1, 0, -1):
                s += l[i]
            s = "-" + s
        else:
            for i in range(len(l)- 1, -1, -1):
                s += l[i]
        if int(s) >= 2**31-1 or int(s) <= -2**31:
            return 0 
        return int(s)
        
