class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for i in range(len(s)):
            res+=(ord(s[len(s)-1-i])-64)*(26**i)
        return res
print(Solution().titleToNumber('AZ'))