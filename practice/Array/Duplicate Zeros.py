class Solution:
    def duplicateZeros(self, a: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        # Time: O(N)
        # Space: O(1)
        
        i, ln = 0, len(a)
        
        while i < ln - 1:
            if a[i] == 0:
                for j in range(ln - 1, i, -1):
                    a[j] = a[j - 1]
                a[j] = 0
                i += 1
            i += 1
