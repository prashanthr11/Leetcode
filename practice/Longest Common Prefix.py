class Solution:
    def longestCommonPrefix(self, a: List[str]) -> str:
        mini = int(1e10)
        ret = ''

        
        for i in a:
            mini = min(mini, len(i))
        if len(a):
            cmp = a[0]

            for i in range(mini):
                for j in a[1:]:
                    if j[i] != cmp[i]:
                        return ret
                ret += cmp[i]

        return ret
