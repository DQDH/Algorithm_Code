class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > -2 ** 31 and x < 2 ** 31 - 1:
            xx=0
            if x > 0:
                s=str(x)
                p=list(reversed(s))
                for i in range(len(p)):
                    xx=xx+int(p[i])*(10**(len(p)-1-i))
                if xx < 2 ** 31 - 1:
                    return xx
                else:
                    return 0
            else:
                s=str(x)
                p=list(reversed(s[1:len(s)]))
                for i in range(len(p)):
                    xx=xx+int(p[i])*(10**(len(p)-1-i))
                if xx *-1> -2 ** 31:
                    return xx*-1
                else:
                    return 0
        else:
            return 0
x=1534236469
a=Solution().reverse(x)
b=1