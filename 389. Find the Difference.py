class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s, t = sorted(s), sorted(t)
        for x, y in zip(s,t):
            if x!=y:
                return y
        return t[-1]
