class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res=0
        rr=max(nums)*3+abs(target)
        length=len(nums)
        nums.sort()
        for i in range(length):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,length-1
            while l<r:
                re=nums[i]+nums[l]+nums[r]
                if abs(re-target)<=rr:
                    rr=abs(re-target)
                    res=re
                    if rr==0:
                        return target
                if re-target<0:
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                else:
                    r-=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return res
print(Solution().threeSumClosest([0,5,-1,-2,4,-1,0,-3,4,-5],1))
