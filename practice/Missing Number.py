class Solution:
    def missingNumber(self, a: List[int]) -> int:
        sumi = sum(a)
        ln = len(a)
        return (ln * (ln + 1) // 2) - sumi
        
