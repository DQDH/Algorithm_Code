class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman=['I','V','X','L','C','D','M']
        Int=[1,5,10,50,100,500,1000]
        s=list(s)
        r=0
        t1=0
        for i in range(len(s)):
            t2=Int[Roman.index(s[i])]
            if t1<t2 :
                r = r + (t2 - 2 * t1)
            else:
                r = r + t2
            t1=t2
        return r
s="XX"
print(Solution().romanToInt(s))