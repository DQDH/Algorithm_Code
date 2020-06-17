class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        tmp=[True]*n
        print(tmp)
        for i in range(2,n):
            if tmp[i]:
                res+=1
                for j in range(2,n):
                    if i*j<n:
                        tmp[i*j]=False
        return res
print(Solution().countPrimes(12))