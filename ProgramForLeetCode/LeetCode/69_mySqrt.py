class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==1:
            return 1
        a = 0
        b = x
        t = x / 2
        while b - t > 0.5:
            if ((t//1)**2==x or (t//1)**2<x)and ((t//1)+1)**2>x:
                return int(t//1)
            if t ** 2 > x:
                b = t
                t = t - (t - a) / 2
            else:
                a = t
                t = t + (b - t) / 2
        return int(t//1)
Solution().mySqrt(7)
