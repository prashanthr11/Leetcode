class Solution:
    
    def col(self, a, j, cmpa):
        
        for i in range(9):
            if cmpa == a[i][j]:
                return False
            
        return True
    
    
    def diagonal(self, a, x, y, cmpa):

        i, j = x, y
        
        while i < x + 3:
            while j < y + 3:
                if cmpa == a[i][j]:
                    return False
                j += 1
            j = y
            i += 1
        
        return True
    
    
    def solveSudoku(self, a):
        """
        Do not return anything, modify board in-place instead.
        """
    
        def solve(a, r, c, tmp):
            for i in range(tmp, 10):
                if str(i) not in a[r]:
                    if self.col(a, j, str(i)):
                        if self.diagonal(a, (r // 3) * 3, (c // 3) * 3, str(i)):
                            return str(i), True
            
            return '', False
        
                
        for i in range(9):
            for j in range(9):
                if a[i][j] == '.':
                    tmp ,isFlag = solve(a, i, j, 1)
                    while isFlag:
                        a[i][j] = tmp
                        if not self.solveSudoku(a):
                            a[i][j] = '.'
                            tmp ,isFlag = solve(a, i, j, int(tmp) + 1)
                        else:
                            return a

                    return False
        return a
