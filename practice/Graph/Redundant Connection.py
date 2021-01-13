class DSU:
    def __init__(self):
        self.parent = list(range(1001))
        self.rank = [0] * 1001
        
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, x, y):
        xx, yy = self.find(x), self.find(y)
        if xx == yy:
            return False
        
        if self.rank[xx] < self.rank[yy]:
            self.parent[xx] = yy
        elif self.rank[xx] > self.rank[yy]:
            self.parent[yy] = xx
        else:
            self.parent[xx] = yy
            self.rank[yy] += 1
        return True

class Solution:
    
    # Time: O(N)
    # Space: O(N)
    
    def findRedundantConnection(self, a: List[List[int]]) -> List[int]:
        dsu = DSU()
        
        for i, j in a:
            if not dsu.union(i, j):
                return [i, j]
