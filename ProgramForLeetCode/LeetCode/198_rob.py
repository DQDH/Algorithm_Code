class Solution(object):
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        res=[[0]*2 for i in range(len(nums))]
        res[0][1]=nums[0]
        for i in range(1,len(nums)):
            res[i][0]=max(res[i-1][0],res[i-1][1])
            res[i][1]=res[i-1][0]+nums[i]
        return max(res[-1])
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last,now=0,0
        for num in nums:
            last,now=now,max(last+num,now)
        return now
Solution().rob([2,1,1,2])