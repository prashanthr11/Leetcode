class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        ln = len(a)
        if ln <= 2:
            return False
        
        i = 0
        while i + 1 < ln:
            if a[i + 1] <= a[i]:
                break
            i += 1
        
        if i == 0:
            return False
        
        if i + 1 == ln:
            return a[i] > a[-1]
        
        while i + 1 < ln:
            if a[i + 1] >= a[i]:
                return False
            i += 1
            
        return True
