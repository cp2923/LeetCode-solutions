class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = set()
        for i in nums:
            if i in n:
                return True
            else:
                n.add(i)
        return False
