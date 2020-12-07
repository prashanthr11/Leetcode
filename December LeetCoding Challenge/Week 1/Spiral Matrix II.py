class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ot = n
        l = [[0 for i in range(n)] for i in range(n)]

        cnt, start, end = 1, 0, n // 2
        x, last = 0, -1

        while start < end:
            i, j = start, start
            while i < n:
                l[j][i] = cnt
                cnt += 1
                i += 1

            n -= 1
            x = n - start
            tmp = 1 + start

            while x:
                l[tmp][i - 1] = cnt
                cnt += 1
                tmp += 1
                x -= 1

            x = n - start
            temp = i - 2
            while x:
                l[last][temp] = cnt
                cnt += 1
                temp -= 1
                x -= 1

            last -= 1
            x = n - 1
            while x - start > 0:
                l[x][j] = cnt
                cnt += 1
                x -= 1

            start += 1

        if ot % 2:
            l[ot // 2][ot // 2] = cnt
            
        return l
