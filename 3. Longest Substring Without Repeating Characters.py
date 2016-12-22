class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = 0
        maxlen = 0
        char = {}
        for i in range(len(s)):
            if s[i] in char and idx <= char[s[i]]:
                idx = char[s[i]] + 1
            else:
                maxlen = max(maxlen, i - idx + 1)
            char[s[i]] = i

        return maxlen
