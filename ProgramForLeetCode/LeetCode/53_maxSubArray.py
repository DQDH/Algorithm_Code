class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums)==1:
        #     return nums[0]
        # res=nums[0]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         res = max(res,sum(nums[i:j]))
        # return res
        n=len(nums)
        res,now=nums[0],nums[0]
        for i in range(1,n):
            now=max(now+nums[i],nums[i])
            res=max(res,now)
        return res
Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])