class CustomStack:

    def __init__(self, sz: int):
        self.l = list()
        self.maxi = sz

    def push(self, x: int) -> None:
        if len(self.l) < self.maxi:
            self.l.append(x)
        

    def pop(self) -> int:
        if len(self.l):
            return self.l.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < len(self.l):
                self.l[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
