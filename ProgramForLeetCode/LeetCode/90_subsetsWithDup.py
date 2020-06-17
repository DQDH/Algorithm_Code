class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def tmp(k,nums):
            if k==0:
                return []
            elif k==1:
                rr=[]
                for e in nums:
                    if [e] not in rr:
                        rr.append([e])
                return rr
            elif k==len(nums):
                return [nums]
            else:
                res_i=[]
                for i in range(len(nums)-k+1):
                    prefix=nums[i]
                    for li in tmp(k-1,nums[i+1:]):
                        if [prefix]+li not in res_i:
                            res_i.append([prefix]+li)
                return res_i
        res=[]
        for l in range(len(nums)+1):
            if l==0:
                res.append([])
            elif l==1:
                for e in nums:
                    if [e] not in res:
                        res.append([e])
            elif l==len(nums):
                res.append(nums)
            else:
                res+=tmp(l,nums)
        return res
print(Solution().subsetsWithDup(list(sorted([4,4,4,1,4]))))
# [[],[4],[3],[3,4],[2],[2,4],[2,3],[2,3,4],[1],[1,4],[1,3],[1,3,4],[1,2],[1,2,4],[1,2,3],[1,2,3,4]]