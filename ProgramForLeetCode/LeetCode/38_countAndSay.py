class Solution(object):
    def say(self,s):
        h=''
        index=0
        for i in range(len(s)):
            if i+1>=len(s):
                num=i+1-index
                h=h+str(num)+str(s[i])
            elif s[i]!=s[i+1]:
                num=i+1-index
                h=h+str(num)+str(s[i])
                index=i+1
        return h
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        h='1'
        if n==1:
            return h
        for i in range(2,n+1):
            h=self.say(h)
        return h
a=Solution().countAndSay(6)
print(a)

