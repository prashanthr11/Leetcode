class Solution:
    def canVisitAllRooms(self, a: List[List[int]]) -> bool:
        
        # Time: O(N) All the elements are visited once. As soon as we completed for the specific index we cache it.
        # Space: O(N)
        
        def solve(idx, a, rec):
            nonlocal l
            
            if idx in rec or not a[idx] or l[idx]:
                return
            
            if not a[idx]:
                return
            
            for i in a[idx]:
                solve(i, a, rec + [idx])
                l[i] = 1
        
        l = [0] * len(a)
        
        solve(0, a, [])
        l[0] = 1
        
        return False if 0 in l else True
