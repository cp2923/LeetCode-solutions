class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        idx=[s.index(l) for l in letters if s.count(l) == 1]
        if len(idx) > 0:
            return min(idx)
        else:
            return -1
