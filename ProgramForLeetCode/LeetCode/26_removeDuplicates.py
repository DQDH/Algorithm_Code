class Solution:
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=0
        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            j=i+1
            if nums[i]!=nums[j]:
                n=n+1
                nums[n]=nums[j]
        return n+1

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)
nums = [1,1,2]
a = Solution().removeDuplicates2(nums)