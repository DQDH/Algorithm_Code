class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            tmp=x
            l=[]
            result=0
            while tmp!=0:
                r=tmp%10
                tmp=tmp//10
                l.append(r)
            for i in range(len(l)):
                result=result+l[i]*(10**(len(l)-i-1))
            return result==x
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            x=str(x)
            y = x[::-1]
            return x==y

a=123
Solution().isPalindrome2(a)