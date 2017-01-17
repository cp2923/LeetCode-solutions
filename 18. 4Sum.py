class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for j in range(len(nums) - 3):
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            for i in range(j + 1, len(nums) - 2):
                if i > j + 1 and nums[i] == nums[i - 1]:
                    continue
                l, r = i + 1, len(nums) - 1
                while l < r:
                    s = nums[j] + nums[i] + nums[l] + nums[r]
                    if s < target:
                        l = l + 1
                    elif s > target:
                        r = r - 1
                    else:
                        result.append((nums[j], nums[i], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l+1]:
                            l = l + 1
                        while l < r and nums[r] == nums[r-1]:
                            r = r - 1
                        l = l + 1
                        r = r - 1
        return result
