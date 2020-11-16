class Solution:
    def countSquares(self, l: List[List[int]]) -> int:
        
        def check(l, st, en):
            return True if 0 not in l[st:en] else False


        def elements(l, r, c, end_r, end_c):
            if len(l) <= end_r or len(l[0]) <= end_c:
                return False

            for i in range(r, end_r + 1):
                if not check(l[i], c, end_c + 1):
                    return False
            return True



        def get(l, r, c, tmp_r, tmp_c):
            ans = 0
            while elements(l, r, c, tmp_r, tmp_c):
                ans += 1
                tmp_c += 1
                tmp_r += 1
            return ans
        
        ret = 0

        for i in range(len(l)):
            for j in range(len(l[0])):
                if l[i][j]:
                    ret += 1 + get(l, i, j, i + 1, j + 1)
        return ret
