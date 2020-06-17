class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n<2:
            return s
        l,r,res=0,0,0
        #odd
        for i in range(n):
            for j in range(min(i+1,n-i)):
                if s[i-j]!=s[i+j]:
                    break
                if 2*j+1>res:
                    res=2*j+1
                    l=i-j
                    r=i+j
        #even
            for j in range(min(i+1,n-i-1)):
                if s[i-j]!=s[i+j+1]:
                    break
                if 2*(j+1)>res:
                    res=2*(j+1)
                    l=i-j
                    r=i+j+1
        return s[l:r+1]
n=int(input())
for i in range(n):
    res=Solution().longestPalindrome(input())
    print(res)