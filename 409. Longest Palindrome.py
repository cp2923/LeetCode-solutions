class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = False
        count = dict()
        summation = 0
        for i in s:
           count.setdefault(i,0)
           count[i] += 1

        for v in count.values():
            if v & 1 == 0:
                summation += v
            else:
                summation += v - 1
                flag = True
        if flag == True:
            return summation +1
        else:
            return summation
