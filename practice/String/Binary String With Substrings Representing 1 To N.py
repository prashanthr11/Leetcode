class Solution:
    def queryString(self, s: str, n: int) -> bool:
        
        # Time: O(N)
        # Space: O(1)
        
        j = 0
        while bin(1 << j)[2:] in s:
            j += 1
            if (1 << j) >= n:
                break

        
        for i in range(j, n + 1):
            if bin(i)[2:] not in s:
                return False
            
        return True
