class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        result = 0
        while x:
            result = result * 10 + x % 10
            x /= 10

        result = result * sign
        if result > 2**31 - 1 or result < -1 *(2**31):
            return 0
        else:
            return result
