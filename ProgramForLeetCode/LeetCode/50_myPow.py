class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            n=-n
            x=1/x
        res=1
        while n:
            if n&1:
                res*=x
            x*=x
            n>>=1
        return res
    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n < 0:
            return 1/self.myPow1(x,-n)
        if n&1:
            return x*self.myPow1(x*x,n>>1)
        else:
            return self.myPow1(x*x,n>>1)
print(Solution().myPow1(2.00000,15))