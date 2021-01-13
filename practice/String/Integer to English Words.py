class Solution:
    def numberToWords(self, a: int) -> str:
        
        # Time: O(N)
        # Space: O(N) 2 Dictionaries are treated as constant space. Because those we independent on input.
        
        def solve(s):
            flag, ret = False, list()
            
            d = {0:'', 1: 'One', 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
            
            d1 = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
            
            a, b, c = int(s[0]), int(s[1]), int(s[2])
            
            if a:
                ret.append(d[a])
                ret.append('Hundred')
                flag = True
                
            if b:
                if b == 1:
                    ret.append(d1[b * 10 + c])
                    
                    return ret, True
                
                ret.append(d1[b])
                flag = True
                
            if c:   
                ret.append(d[c])
                flag = True
                
            return ret, flag
            
            
        if not a:
            return 'Zero'
        
        s = str(a)
        if len(s) % 3:
            s = ('0' * (3 - len(s) % 3)) + s
        
        l = ['Billion', 'Million', 'Thousand', '']
        l.reverse()
        ret = list()
        
        for i in range(0, len(s), 3):
            tmp, isflag = solve(s[i:i + 3])
            ret += tmp
            if isflag and 0 < len(s[i + 3::3]) < len(l):
                ret.append(l[len(s[i + 3::3])])
                
        tmp = ''
        for i in ret:
            tmp += i + ' '
            
        return tmp[:-1]
