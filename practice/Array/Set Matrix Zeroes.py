class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Time: O(N * M) where N and M are rows and the columns in the matrix
        # Space: O(1) Maybe we could use some 2 ** 32 value in place of -12345

        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 0:
                    for k in range(len(a[i])):
                        a[i][k] = -12345 if a[i][k] else 0
                        
                    for x in range(len(a)):
                        a[x][j] = -12345 if a[x][j] else 0
                    a[i][j] = -12345
                        
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == -12345:
                    a[i][j] = 0
