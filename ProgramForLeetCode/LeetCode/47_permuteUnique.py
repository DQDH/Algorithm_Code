class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [nums]
        res=[]
        for i in range(len(nums)):
            if i >0 and nums[i] in nums[:i]:
                continue
            prefix=nums[i]
            rest=nums[:i]+nums[i+1:]
            for j in self.permuteUnique(rest):
                res.append([prefix]+j)
        return res
print(Solution().permuteUnique([3,3,0,3]))