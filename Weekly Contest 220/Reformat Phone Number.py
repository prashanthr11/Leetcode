class Solution:
    def reformatNumber(self, a: str) -> str:
        '''
        
        # Time: O(n)
        # Space: O(n)
        
        a = a.replace('-', '').replace(' ', '')
        def helper(a, ln, ret):
            if ln <= 3:
                return (ret + '-' + a)[1:]
            if ln == 4:
                return (ret + '-' + a[:2] + '-' + a[2:])[1:]
            else:
                return helper(a[3:], ln - 3, ret + '-' + a[:3])
            
        return helper(a, len(a), '')
    
        '''
        
        # Time: O(n)
        # Space: O(1)
        
        a = a.replace('-', '').replace(' ', '')

        ln = len(a)
        ret = ''
        
        for i in range(0, ln, 3):
            ret += a[i:i + 3] + '-'
        
        if ln - i == 1:
            tmp = ret[-4:]
            ret = ret[:-4] + '-' + tmp[::2] + '-'
            
        return ret[:-1]
