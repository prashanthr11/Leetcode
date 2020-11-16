from collections import deque as dq

class RecentCounter:

    def __init__(self):
        self.l = dq()
        

    def ping(self, t: int) -> int:
        self.l.append(t)

        while self.l[0] < t - 3000:
            self.l.popleft()
            
        return len(self.l)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
