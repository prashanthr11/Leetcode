class Solution:
    def threeConsecutiveOdds(self, a: List[int]) -> bool:
        
        def helper(a):
            for i in a:
                if not i % 2:
                    return True
            return False
        
        for i in range(len(a) - 2):
            if not helper(a[i:i + 3]):
                return True
            
        return False
                
        
