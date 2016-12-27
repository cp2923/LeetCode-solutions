class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenS = len(s)
        summation = 0
        for i in range(0,lenS):
            n = ord(s[lenS - i - 1]) - 64
            summation = n*26**i + summation
        return summation
