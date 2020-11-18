class NumMatrix:

    def __init__(self, a: List[List[int]]):
        if len(a):
            ln = len(a[0])
            self.prefix = list()

            for i in range(len(a)):
                tmp = [0] * (ln + 1)
                for j in range(ln):
                    tmp[j + 1] = tmp[j] + a[i][j]
                self.prefix.append(tmp)


    def sumRegion(self, a: int, b: int, c: int, d: int) -> int:
        sumi = 0
        for i in range(a, c + 1):
            sumi += self.prefix[i][d + 1] - self.prefix[i][b]
        return sumi


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
