class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str = str.strip()
        length = len(str)
        if length == 0:
            return 0

        if str[0] == '-' or str[0] == '+':
            i = 1
        else:
            i = 0

        result = 0
        while i < length and str[i].isdigit():
            result = result * 10 + int(str[i])
            i += 1

        if str[0] == '-':
            return max(-2147483648,-result)

        return min(2147483647, result)
