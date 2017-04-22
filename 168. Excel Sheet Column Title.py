class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''
        result = ''
        while n > 0:
            tmp = n % 26
            n = n / 26
            if tmp > 0:
                result = chr(ord('A') + tmp - 1) + result
            else:
                result = 'Z' + result
                n -= 1
        return result
