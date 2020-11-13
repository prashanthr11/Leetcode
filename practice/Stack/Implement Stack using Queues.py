class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ln = 0
        self.l = list()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.l.append(x)
        self.ln += 1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.ln -= 1
        return self.l.pop(len(self.l) - 1)
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.l[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.ln == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
