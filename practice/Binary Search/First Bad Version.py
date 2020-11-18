# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        mini = n + 1
        i, j = 0, n
        while i <= j:
            mid = (i + j) // 2
            if isBadVersion(mid):
                mini = min(mini, mid)
                j = mid - 1
            else:
                i = mid + 1
        return mini
        
