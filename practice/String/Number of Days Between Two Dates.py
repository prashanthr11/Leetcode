class Solution:
    def daysBetweenDates(self, a, b):
        
        # Time: O(1)
        # Space: O(1)
        
        def isleap(year):
            if year % 4 == 0 and year % 100 != 0:
                return True
            if year % 400 == 0:
                return True
            return False
        
        
        y1, m1, d1 = map(int, a.split('-'))
        y2, m2, d2 = map(int, b.split('-'))
        cnt = 0
        l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        for i in range(min(y1, y2), max(y1, y2)):
            if isleap(i):
                cnt += 366
            else:
                cnt += 365
        
        if y1 <= y2:
            for i in range(m1 - 1):
                if i == 1 and isleap(y1):
                    cnt -= 29
                else:
                    cnt -= l[i]
                
            for i in range(m2 - 1):
                if i == 1 and isleap(y2):
                    cnt += 29
                else:
                    cnt += l[i]

            cnt -= d1
            cnt += d2
            
            return abs(cnt)
        else:
            for i in range(m2 - 1):
                if i == 1 and isleap(y2):
                    cnt -= 29
                else:
                    cnt -= l[i]
                
            for i in range(m1 - 1):
                if i == 1 and isleap(y1):
                    cnt += 29
                else:
                    cnt += l[i]
                
            cnt += d1
            cnt -= d2
            
            return abs(cnt)
