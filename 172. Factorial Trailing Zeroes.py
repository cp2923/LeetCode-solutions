class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        power = 1
        fives = n / (5 ** power)
        while fives:
            result += fives
            power += 1
            fives = n / (5 ** power)
        return result
