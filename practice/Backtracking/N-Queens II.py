class Solution:
    def totalNQueens(self, n: int) -> int:
        
        # Time: O(N!) where n is the size of the chess board.
        # Space: O(N ** 2) Keeping track of all possitions in N * N board.
        
        def solve(board, idx):

            nonlocal total_possibilities
            
            if idx >= len(board):
                board_copy = [i for i in board]
                total_possibilities.append(board_copy)
                
                return False
            
            for i in range(len(board)):
                
                if can_place(board, idx, i):
                    board[idx][i] = 1
                    
                    if solve(board, idx + 1):
                        return True
                    
                    board[idx][i] = 0
                
            return False
        
        def can_place(board, row, col):
            
            ln = len(board)
            
            # Checking for Queen in the same row
            if 1 in board[row]:
                return False
            
            # Checking for Queen in the same column
            for column in range(ln):
                if board[column][col]:
                    return False
                
            # Checking for Queen in Left and Right Upper and Lower Diagonals
            x, y, i, j = row, col, row, col
            
            while x >= 0 and y >= 0:
                if board[x][y]:
                    return False
                
                x -= 1
                y -= 1
                
            while i < ln and j < ln:
                if board[i][j]:
                    return False
                
                i += 1
                j += 1
                
            x, y, i, j = row, col, row, col
            
            while x >= 0 and y < ln:
                if board[x][y]:
                    return False
                
                x -= 1
                y += 1
                
            while i < ln and j >= 0:
                if board[i][j]:
                    return False
                
                i += 1
                j -= 1
                
            return True
                
        
        board = [[0] * n for i in range(n)]
        total_possibilities = list()
        solve(board, 0)
        
        return len(total_possibilities)
