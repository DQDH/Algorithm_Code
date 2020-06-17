class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)-1
        result=0
        for si in s:
            result=(ord(si)-64)*(26**l)+result
            l=l-1
        return result
Solution().titleToNumber("ZY")