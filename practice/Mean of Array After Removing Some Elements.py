class Solution:
    def trimMean(self, l: List[int]) -> float:
        l.sort()
        maxi, mini = int(len(l) * .95), int(len(l) * .05)
        return sum(l[mini:maxi]) / len(l[mini:maxi])
