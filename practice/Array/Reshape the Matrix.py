class Solution:
    def matrixReshape(self, a: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        # Time: O(N) where N is the total number of elements
        # Space: O(N)

        i, j = len(a), len(a[0])
        
        if i * j != r * c:
            return a
        
        ret = [[0] * c for i in range(r)]
        col, row = 0, 0
        
        for i in a:
            for j in i:
                ret[row][col] = j
                col += 1
                
                if col >= len(ret[0]):
                    col = 0
                    row += 1
        
        return ret
