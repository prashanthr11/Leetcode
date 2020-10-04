class Solution:
    def specialArray(self, a: List[int]) -> int:
        def solve(l, i):
            cnt = 0
            for j in l:
                if j >= i:
                    cnt += 1
            return cnt
        
        for i in range(len(a) + 1):
            if i == solve(a, i):
                return i
        return -1
