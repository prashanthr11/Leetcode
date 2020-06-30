class Solution:
    def canArrange(self, a: List[int], k: int) -> bool:
        return sum(a) % k == 0
