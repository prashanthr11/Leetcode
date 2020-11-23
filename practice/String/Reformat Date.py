class Solution:
    def reformatDate(self, a: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        a = a.split()
        
        mnth = str(1 + month.index(a[1]))
        
        if len(mnth) == 1:
            mnth = '0' + str(1 + month.index(a[1]))
            
        day = a[0][:-2]
        if len(day) == 1:
            day = '0' + str(a[0][:-2])
            
        return str(a[-1] + '-' + mnth + '-' + day)
