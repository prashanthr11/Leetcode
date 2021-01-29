class Solution:
    
    # Time: O(Log N)
    # Space: O(1)
    
    def searchMatrix(self, a, t):
        r, c = len(a), len(a[0])
        i, j = 0, r * c - 1
        
        while i <= j:
            mid = i + (j - i) // 2
            if a[mid // c][mid % c] == t:
                return True
            
            if a[mid // c][mid % c] > t:
                j = mid - 1
            else:
                i = mid + 1
            
        return False
