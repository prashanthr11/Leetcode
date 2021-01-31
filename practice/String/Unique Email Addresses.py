class Solution:
    
    # Time: O(N)
    # Space: O(N)
    
    def check(self, s):
        tmp = ''
        
        l = s.split('@')
        for i in l[0]:
            if i == '+':
                break
            if i == '.':
                continue
            tmp += i
            
        tmp += '@' + l[1]
        self.st.add(tmp)
        
        
    def numUniqueEmails(self, s: List[str]) -> int:
        self.st = set()
        
        for i in s:
            self.check(i)
    
        return len(self.st)
