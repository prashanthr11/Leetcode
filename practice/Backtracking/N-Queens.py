class Solution:
    def solveNQueens(self, n):
        
        # Time: O(N!) where n is the size of the chess board.
        # Space: O(N ** 2) Keeping track of all possitions in N * N board.
        
        def solve(board, a):
            if a >= len(board):     # Base case: When all Queens are placed.
                nonlocal ret
                tmp = [''.join(i) for i in board]
                ret.append(tmp)
                
                return False        # Backtracking
        
            for i in range(n):
                if can_place(board, a, i):      # Checking if Queen can be placed at board[a][i]
                    board[a][i] = 'Q'

                    if solve(board, a + 1):     # Recursive call for placing next Queen
                        return True
                        
                    board[a][i] = '.'       # Remove Queen at board[a][i] (BackTracking)
                    
            return False            # Returns False when Queen cannot be placed in a single row.


        def can_place(board, a, b):
            
            ln = len(board)
            
            if 'Q' in board[a]:     # Checking in a Row
                return False
                
            for k in range(ln):     # Checking in Column b
                if board[k][b] == 'Q':
                    return False
            
            x, y = a, b
            i, j = a, b
            
            # Checking for a Queen in Left Upper Diagonal
            
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
            
                i -= 1
                j -= 1
            
            
            # Checking for a Queen in Left Bottom Diagonal
            
            while y >= 0 and x < ln:
                if board[x][y] == 'Q':
                    return False
            
                x += 1
                y -= 1
                
            x, y = a, b
            i, j = a, b
            
            # Checking for a Queen in Right Bottom Diagonal
            
            while i < ln and j < ln:
                if board[i][j] == 'Q':
                    return False
                    
                i += 1
                j += 1
                
            
            # Checking for a Queen in Right Upper Diagonal
            
            while x >= 0 and y < ln:
                if board[x][y] == 'Q':
                    return False
                
                x -= 1
                y += 1
            
            return True
        
        board = [['.'] * n for i in range(n)]
        ret = list()
        
        solve(board, 0)
        
        return ret
