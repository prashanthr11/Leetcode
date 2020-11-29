from collections import deque as dq
from itertools import islice

class FrontMiddleBackQueue:

    def __init__(self):
        self.l = dq()

    def pushFront(self, val: int) -> None:
        self.l.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        self.l.insert(len(self.l) // 2, val)

    def pushBack(self, val: int) -> None:
        self.l.append(val)

    def popFront(self) -> int:
        if len(self.l):
            return self.l.popleft()
        return -1

    def popMiddle(self) -> int:
        if len(self.l):
            mid = len(self.l) // 2
            if len(self.l) % 2:
                tmp = self.l[mid]
            else:
                mid -= 1
                tmp = self.l[mid]
            x = dq(islice(self.l, 0, mid))
            x += dq(islice(self.l, mid + 1, len(self.l)))
            self.l = x
            return tmp
        return -1

    def popBack(self) -> int:
        if len(self.l):
            return self.l.pop()
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
