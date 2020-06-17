class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=len(nums)/2
        num_unique=list(set(nums))
        for i in num_unique:
            if nums.count(i)>num:
                return i
Solution().majorityElement([2,2,1,1,1,2,2])