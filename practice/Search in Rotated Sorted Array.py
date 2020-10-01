class Solution:
    def search(self, a: List[int], b: int) -> int:
        try:
            return a.index(b)
        except ValueError:
            return -1
        
