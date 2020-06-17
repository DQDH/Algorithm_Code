class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #chaoshi
        # length=len(nums)
        # res = []
        # for i in range(length):
        #     n1=nums[i]
        #     for j in range(i+1,length-1):
        #         n2=nums[j]
        #         n3=-(n1+n2)
        #         if n3 in nums[j+1:]:
        #             res.append([n1,n2,n3])
        # res1 = [set(res_i) for res_i in res]
        # for i in range(len(res1)-1):
        #     if res1[i] in res1[i+1:]:
        #         res[i]=[]
        # while [] in res:
        #     res.remove([])
        res,n=[],len(nums)
        nums.sort()
        for i in range(n):
            if i >0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while l<r:
                re=nums[i]+nums[l]+nums[r]
                if re==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif re<0:
                        l+=1
                else:
                    r-=1
        return res
Solution().threeSum([-1,0,1,2,-1,-4])