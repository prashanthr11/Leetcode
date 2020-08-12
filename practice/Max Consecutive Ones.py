class Solution:
    def findMaxConsecutiveOnes(self, a: List[int]) -> int:
        cnt = 0
        ret = 0
        for i in a:
            if i:
                cnt += 1
            else:
                ret = max(ret, cnt)
                cnt = 0
        return max(cnt, ret)
