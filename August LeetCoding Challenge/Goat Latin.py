class Solution:
    def toGoatLatin(self, a: str) -> str:
        ret = list()
        b = "aeiouAEIOU"
        l = a.split()
        for i in range(len(l)):
            if l[i][0] in b:
                s = l[i] + "ma" + "a" * (i + 1)
            else:
                s = l[i][1:]
                s += l[i][0] + "ma" + "a" * (i + 1)
            ret.append(s)
        ans = ""
        for i in ret:
            ans += i + " "
        return ans[:-1]
