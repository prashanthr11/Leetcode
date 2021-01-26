class NumArray:
    
    # Time: O(N Log N)
    # Space: O(N)

    def __init__(self, a: List[int]):
        self.a = a
        self.ft = [0] * (len(a) + 1)
        self.createft(a)
    
    def createft(self, l):
        for i, a in enumerate(l):
            self.updateft(i, a)
            
    def updateft(self, i, diff):
        i += 1
        while i <= len(self.a):
            self.ft[i] += diff
            i += (i & -i)
        
        
    def getsum(self, l):
        sumi = 0
        l += 1
        while l > 0:
            sumi += self.ft[l]
            l -= (l & -l)
        
        return sumi
    
    def update(self, index: int, val: int) -> None:
        diff = val - self.a[index]
        self.a[index] = val
        self.updateft(index, diff)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.getsum(right) - self.getsum(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
