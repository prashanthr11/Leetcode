from collections import Counter
class Solution:
    def isPathCrossing(self, a: str) -> bool:
        l = list()
        (x, y) = (0, 0)
        l.append((x, y))
        for i in a:
            if i == "E":
                l.append((l[-1][0] + 1, l[-1][1]))
            if i == "W":
                l.append((l[-1][0] - 1, l[-1][1]))
            if i == "N":
                l.append((l[-1][0], l[-1][1] + 1))
            if i == "S":
                l.append((l[-1][0], l[-1][1] - 1))
        d = Counter(l)
        if len(set(d.values())) > 1:
            return True
        else:
            return False
