class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff = 0
        while x or y:
            diff = diff + ((x % 2) ^ (y % 2))
            x = x / 2
            y = y / 2
        return diff
