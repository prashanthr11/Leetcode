class Solution:
    def evalRPN(self, a: List[str]) -> int:
        
        # Time: O(N)
        # Space: O(N / 2) --> O(N) as there will be n + 1 intergers in the list
        
        def solve(a, i, b):
            if i == '/':
                return int(a / b)
            
            if i == '+':
                return a + b
            
            if i == '-':
                return a - b
            
            return a * b
        
        s = '+-/*'
        l = list()
        
        for i in a:
            if i in s:
                y = l.pop()
                x = l.pop()
                tmp = solve(int(x), i, int(y))
                l.append(str(tmp))
            else:
                l.append(i)
        
        return l[0]
