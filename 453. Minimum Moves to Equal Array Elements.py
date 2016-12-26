class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minn = min(nums)
        m = 0
        for n in nums:
            m += n - minn
        return m
