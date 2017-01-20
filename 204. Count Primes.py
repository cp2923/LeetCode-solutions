class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        i = 2
        while i ** 2 < n:
            if prime[i]:
                j = 2 * i
                while j < n:
                    prime[j] = False
                    j += i
            i += 1

        return sum(prime)
