from string import ascii_lowercase as lc

class Solution:
    def alphabetBoardPath(self, a: str) -> str:
        ret, s = '', lc
        cur = (0, 0)
        
        for i in a:
            ind = s.find(i)
            x = ind // 5
            y = ind - (5 * x)

            x_dist, y_dist = x - cur[0], y - cur[1]

            if cur[0] == 5 and x_dist < 0:
                ret += 'U'
                x_dist += 1
            
            if y_dist > 0:
                ret += 'R' * y_dist
            else:
                ret += 'L' * abs(y_dist)

            if x_dist > 0:
                ret += 'D' * x_dist
            else:
                ret += 'U' * abs(x_dist)

            ret += '!'
            cur = (x, y)
            
        return ret
