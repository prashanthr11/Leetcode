class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = list()
        for i in s:
            if len(l) == 0:
                l.append(i)
            elif l[-1] == i:
                l.pop()
            else:
                l.append(i)
        return ''.join(l)
