class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)
            for i in range(len(nums)-1):
                if nums[i]<target and nums[i+1]>target:
                    return i+1
    def searchInsert2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        if target>nums[n-1]:
            return n
        for k in range(n):
            if target<=nums[k]:
                return k