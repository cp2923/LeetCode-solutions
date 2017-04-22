class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        i = 1
        squares = []
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1
        res = 0
        check = {n}
        while check:
            res += 1
            tmp = set()
            for x in check:
                for y in squares:
                    if x == y:
                        return res
                    if x < y:
                        break
                    tmp.add(x-y)
            check = tmp
        return res
