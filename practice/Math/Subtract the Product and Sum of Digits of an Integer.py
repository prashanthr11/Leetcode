class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro, ret = 1, 0
        for i in str(n):
            pro *= int(i)
            ret += int(i)
        return pro - ret
