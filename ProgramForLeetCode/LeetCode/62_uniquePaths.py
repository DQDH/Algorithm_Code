class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=[1]*m
        for i in range(1,n):
            for j in range(1,m):
                res[j]+=res[j-1]
        return res[-1]
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=[[1]*m for k in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                res[i][j]=res[i-1][j]+res[i][j-1]
        return res[-1][-1]
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #chaoshi
        if m==1 or n==1:
            return 1
        else:
            return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
print(Solution().uniquePaths(7,3))