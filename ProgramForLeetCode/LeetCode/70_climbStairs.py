class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[1,1]
        t=n-3
        if n<3:
            return n
        else:
            while t>0:
                t=t-1
                tmp=a[0]
                a[0]=a[0]+a[1]
                a[1] = tmp
            r=a[0]*2+a[1]
        return r
Solution().climbStairs(5)