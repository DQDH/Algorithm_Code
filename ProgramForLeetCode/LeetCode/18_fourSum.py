class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length=len(nums)
        if length<4:
            return []
        nums.sort()
        res=[]
        for i in range(length):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,length):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l,r=j+1,length-1
                while l<r:
                    rr=nums[i]+nums[j]+nums[l]+nums[r]
                    if rr-target==0:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif rr-target>0:
                        r-=1
                    else:
                        l+=1
        return res
print(Solution().fourSum([-1,0,-5,-2,-2,-4,0,1,-2],-9))