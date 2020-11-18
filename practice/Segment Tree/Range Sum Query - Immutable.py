class NumArray:

    def __init__(self, a: List[int]):
        if len(a):
            self.prefix = [0] * len(a)
            self.prefix[0] = a[0]
        
        for i in range(1, len(a)):
            self.prefix[i] += self.prefix[i - 1] + a[i]

    def sumRange(self, i: int, j: int) -> int:
        if len(self.prefix):
            if i == 0:
                return self.prefix[j]
            return self.prefix[j] - self.prefix[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
