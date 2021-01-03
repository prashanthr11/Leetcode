class Solution:
    def maximumUnits(self, a: List[List[int]], b: int) -> int:
        
        # Time: O(N LogN)
        # Space: O(1)
        
        ans = 0
        a.sort(key = lambda x:x[1], reverse = True)
        boxes = b
        
        for k, v in a:
            if boxes == 0:
                break
            if boxes - k >= 0:
                ans += (k * v)
                boxes -= k
            elif boxes - k < 0:
                ans += (boxes * v)
                break
        
        return ans
