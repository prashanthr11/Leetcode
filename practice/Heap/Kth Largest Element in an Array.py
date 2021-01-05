from heapq import heapify, nlargest

class Solution:
    def findKthLargest(self, a: List[int], k: int) -> int:
        
        # Time: O(N)
        # Space: O(1)
        
        heapify(a)
        return nlargest(k, a)[-1]
