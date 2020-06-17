class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        i=0
        res=''
        r=chr(64+n%26)
        n-=n%26
        while True:
            if 26**i>n:
                break
            else:
                i+=1
        for j in range(i,0,-1):
            num=n//(26**(j-1))
            n-=num*26**(j-1)
            res+=chr(64+num)
        return res+r
print(Solution().convertToTitle(701))