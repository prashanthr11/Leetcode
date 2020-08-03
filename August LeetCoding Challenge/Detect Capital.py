class Solution:
    def detectCapitalUse(self, a: str) -> bool:
        if a.istitle() or a.isupper() or a.islower():
            return True
        return False
        
        
