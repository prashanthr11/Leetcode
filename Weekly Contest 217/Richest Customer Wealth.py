class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        sumi = 0
        for i in a:
            sumi = max(sumi, sum(i))
            
        return sumi
