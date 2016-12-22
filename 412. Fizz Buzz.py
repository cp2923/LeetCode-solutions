class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        words = []
        for i in range(1,n+1):
            if i % 15 == 0:
                words.append("FizzBuzz")
            elif i % 3 == 0:
                words.append("Fizz")
            elif i % 5 == 0:
                words.append("Buzz")
            else:
                words.append(str(i))
        return words
