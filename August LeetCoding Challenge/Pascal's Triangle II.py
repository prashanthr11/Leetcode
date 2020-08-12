class Solution:
    def getRow(self, a: int) -> List[int]:
        l=list()
        for i in range(a + 1):
            l.append([1 for j in range(i + 1)])
        i = 1
        while i <= a:
            for j in range(1, len(l[i]) - 1):
                l[i][j] = l[i-1][j-1]+l[i-1][j]
            i += 1
        return l[-1]
