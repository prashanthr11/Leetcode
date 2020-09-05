class Solution:
    def diagonalSum(self, a: List[List[int]]) -> int:
        cnt, i, j = 0, 0, len(a) - 1
        while i < len(a):
            cnt += a[i][j] + a[i][i]
            i += 1
            j -= 1
            
        if len(a) % 2:
            cnt -= a[len(a) // 2][len(a) // 2]

        return cnt
        