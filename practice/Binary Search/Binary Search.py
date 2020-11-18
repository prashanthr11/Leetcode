class Solution:
    def search(self, a: List[int], t: int) -> int:
        i, j = 0, len(a) - 1
        
        while i <= j:
            mid = (i + j) // 2
            if a[mid] == t:
                return mid
            elif a[mid] < t:
                i = mid + 1
            else:
                j = mid - 1
                
        return -1
