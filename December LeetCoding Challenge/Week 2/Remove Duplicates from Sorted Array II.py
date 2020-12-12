class Solution:
    def removeDuplicates(self, l: List[int]) -> int:
        ln = len(l)
        if ln > 1:
            i = 1
            while i < ln:
                j = i + 1
                if l[i] == l[i - 1]:
                    while j < ln and l[j] <= l[i]:
                        j += 1
                    if j == ln:
                        return 1 + i
                    if j == i + 1:
                        i += 1
                    else:
                        i += 1
                        l[i] = l[j]
                        l[j] = -9879879
                else:
                    while j < ln and l[j] < l[i]:
                        j += 1
                    if j == ln:
                        return i + 1
                    if j == i + 1:
                        i += 1
                    else:
                        i += 1
                        l[i] = l[j]
                        l[j] = -9879879
        return ln
