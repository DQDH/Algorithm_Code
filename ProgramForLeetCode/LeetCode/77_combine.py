class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        r, ri = [], []
        self.c(n, k, r, ri, 0)
        return r

    def c(self, n, k, r, ri, ki):
        if k == 0:
            r.append(ri)
            return
        for i in range(ki + 1, n - k + 2):
            self.c(n, k - 1, r, ri + [i], i)
        return
    def helper(self,nums,n,k):
        if k==1:
            res_=[]
            for p in nums:
                res_.append([p])
            return res_
        res=[]
        for i in range(n):
            if len(nums[i:])<k:
                break
            prefix=nums[i]
            for j in self.helper(nums[i+1:],n-1,k-1):
                res.append([prefix]+j)
        return res
    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n==0:
            return [[]]
        nums=[i for i in range(1,n+1)]
        res=self.helper(nums,n,k)
        return res
print(Solution().combine(4,3))