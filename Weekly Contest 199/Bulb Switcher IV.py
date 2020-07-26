class Solution:
    def minFlips(self, a: str) -> int:
        ans = ["0" for i in range(len(a))]
        cnt = 0
        if a[0] != ans[0]:
            cnt += 1
        for i in range(1, len(a)):
            if a[i] != a[i - 1]:
                cnt += 1
        return cnt