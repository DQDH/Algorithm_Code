class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        nums.sort()
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[len(nums)-2]!=nums[len(nums)-1]:
            return nums[len(nums)-1]
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)))*2-sum(nums)
Solution().singleNumber2([2,2,1])