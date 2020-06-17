class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''

        factorial = [1] * (n + 1)
        # factorial[] = [1, 1, 2, 6, 24, ... n!]
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i
        # create a list of numbers to get indices
        nums = [i for i in range(1, n + 1)]
        # because we start from index 0
        k -= 1
        for i in range(1, n + 1):
            # this is the idx of first num each time we will get
            idx = k / factorial[n - i]
            res += str(nums[int(idx)])
            # delete this num, since we have got it
            nums.pop(int(idx))
            # update k
            k -= idx * factorial[n - i]
        return res
    def getPermutation1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        #chaoshi
        def Permutation(Init):
            res=[]
            if len(Init)==1:
                return Init
            for i in range(len(Init)):
                perfix=Init[i]
                for j in Permutation(Init[:i]+Init[i+1:]):
                    res.append(perfix+j)
            return res
        Init = ''
        res = []
        for j in range(1,n+1):
            Init = Init + str(j)
        if len(Init)==1:
            return Init
        for i in range(n):
            prefix=Init[i]
            for last_i in Permutation(Init[:i]+Init[i+1:]):
                res.append(prefix+last_i)
            if len(res) >= k:
                return res[k - 1]
print(Solution().getPermutation(3,3))