class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend > divisor:
            i, tmp = 1, divisor
            while dividend >= tmp:
                dividend -= tmp
                result += i
                i <<= 1
                tmp <<= 1
        if negative:
            result = -result
        return min(max(-2**31, result), 2**31)
