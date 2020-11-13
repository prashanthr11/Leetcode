class SubrectangleQueries:

    def __init__(self, a: List[List[int]]):
        self.l = a
        

    def updateSubrectangle(self, r1: int, c1: int, r2: int, c2: int, qw: int) -> None:
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                self.l[i][j] = qw

    def getValue(self, row: int, col: int) -> int:
        return self.l[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
