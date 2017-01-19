class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1]
        p2, p3, p5 = 0, 0, 0
        while n > 1:
            m2 = result[p2] * 2
            m3 = result[p3] * 3
            m5 = result[p5] * 5
            m = min(m2, m3, m5)
            result.append(m)
            if m == m2:
                p2 += 1
            if m == m3:
                p3 += 1
            if m == m5:
                p5 += 1
            n -= 1
        return result[-1]
