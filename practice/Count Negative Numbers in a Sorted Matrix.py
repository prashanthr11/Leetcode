class Solution:
    def countNegatives(self, a: List[List[int]]) -> int:
        cnt = 0
        
        for i in a:
            for j in i[::-1]:
                if not j >= 0:
                    cnt += 1
                else:
                    break
        return cnt
