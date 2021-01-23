class Solution:
    def largestAltitude(self, a: List[int]) -> int:
        
        # Time: O(N)
        # Space: O(1)
        
        maxi = 0
        prev = 0
        for i in a:
            prev += i
            maxi = max(maxi, prev)
            
        return maxi
