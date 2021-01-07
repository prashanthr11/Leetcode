class Solution:
    def gameOfLife(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # Time: O(N ^ 2)
        # Space: O(1)
        
        neighbours = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
        
        for i in range(len(a)):
            for j in range(len(a[0])):
                sumi = 0
                for x, y in neighbours:
                    if 0 <= i + x < len(a) and 0 <= j + y < len(a[0]):
                        sumi += (a[i + x][j + y] & 1)
                
                sumi -= (a[i][j] & 1)
                
                if a[i][j]:
                    if sumi == 2 or sumi == 3:
                        a[i][j] = 3
                    else:
                        a[i][j] = 1
                else:
                    if sumi == 3:
                        a[i][j] = 2
                        
                        
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] >>= 1
            
