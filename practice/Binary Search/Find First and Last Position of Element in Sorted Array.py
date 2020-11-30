from bisect import bisect, bisect_left

class Solution:
    def searchRange(self, a: List[int], t: int) -> List[int]:
        if not a:
            return [-1, -1]
        
        left, right = bisect_left(a, t), bisect(a, t)
        return [left, right - 1] if right > left else [-1, -1]
