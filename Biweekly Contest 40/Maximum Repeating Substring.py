class Solution:
    def maxRepeating(self, a: str, b: str) -> int:
        cnt = 0
        tmp = b
        while b in a:
            cnt += 1
            b += tmp
        return cnt if cnt else 0
