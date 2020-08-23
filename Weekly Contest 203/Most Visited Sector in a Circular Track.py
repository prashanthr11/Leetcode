class Solution:
    def mostVisited(self, n: int, b: List[int]) -> List[int]:
        ret = list()
        ans = [0 for i in range(n)]
        ans[b[0]-1] = 1
        for i in range(1, len(b)):
            if b[i-1] > b[i]:
                for k in range(b[i-1], b[i] + n):
                    ans[(k) % n] += 1
            else:
                for k in range(b[i - 1], b[i]):
                    ans[k] += 1
        maxi = max(ans)
        for i in range(len(ans)):
            if ans[i] == maxi:
                ret.append(i + 1)
        return ret
