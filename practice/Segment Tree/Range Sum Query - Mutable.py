class NumArray:

    def __init__(self, a: List[int]):
        def build_segment_tree(ind, a, sg, low, high):
            if low == high:
                sg[ind] = a[low]
                return sg[ind]
            
            mid = (low + high) // 2
            build_segment_tree(2 * ind + 1, a, sg, low, mid)
            build_segment_tree(2 * ind + 2, a, sg, mid + 1, high)
            
            sg[ind] = sg[2 * ind + 1] + sg[2 * ind + 2]
            
        self.a = a
        self.sg = [0] * (4 * len(a))
        if len(a):
            build_segment_tree(0, self.a, self.sg, 0, len(a) - 1)
            

    def update(self, i: int, val: int) -> None:
        def abc(ind, start, end, x, y, newValue):
            if start == x and end == y:
                self.sg[ind] += newValue
                return self.sg[ind]
            if start > x or end < y:
                return 0

            mid = (start + end) // 2
            if x <= mid:
                abc(2 * ind + 1, start, mid, x, y, newValue)
            else:
                abc(2 * ind + 2, mid + 1, end, x, y, newValue)

            self.sg[ind] += newValue
        
        abc(0, 0, len(self.a) - 1, i, i, val - self.a[i])
        self.a[i] = val
        

    def sumRange(self, i: int, j: int) -> int:
        def sumi(ind, start, end, i, j):
            if start >= i and j >= end:
                return self.sg[ind]
            
            if i > end or j < start:
                return 0
            
            mid = (start + end) // 2
            
            return sumi(2 * ind + 1, start, mid, i, j) + sumi(2 * ind + 2, mid + 1, end, i, j)
        
        return sumi(0, 0, len(self.a) - 1, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
