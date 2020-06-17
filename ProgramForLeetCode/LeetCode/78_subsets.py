class Solution(object):
    def helper(self,nums,k):
        if k==1:
            res_=[]
            for nums_i in nums:
                res_.append([nums_i])
            return res_
        res=[]
        for i in range(len(nums)):
            if len(nums[i:])<k:
                break
            prefix = nums[i]
            for j in self.helper(nums[i + 1:],k-1):
                res.append([prefix] + j)
        return res
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        for k in range(len(nums)+1):
            if k==0:
                res.append([])
            else:
                res+=self.helper(nums,k)
        return res
print(Solution().subsets([]))