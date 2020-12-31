from heapq import nsmallest

class Solution:
    def kClosest(self, a: List[List[int]], k: int) -> List[List[int]]:
        
        # Method 2
        # Time: O(N Log K) where N is the for building heap and Log k for  heapify
        # Space: O(k)
        
        return nsmallest(k, a, lambda x: x[0] ** 2 + x[1] ** 2)
