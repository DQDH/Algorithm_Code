class Solution(object):
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(nums, 0)
        return self.res

    def helper(self, nums, i):
        nums1 = nums[:]
        if i == (len(nums1) - 1):
            self.res.append(nums1)
            return
        for l in range(i, len(nums)):
            nums1[i], nums1[l] = nums1[l], nums1[i]
            self.helper(nums1, i + 1)
            nums1[i], nums1[l] = nums1[l], nums1[i]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            prefix = nums[i]
            rest = nums[:i] + nums[i + 1:]
            for j in self.permute(rest):
                res.append([prefix] + j)
        return res
print(Solution().permute([1,2,3,4]))