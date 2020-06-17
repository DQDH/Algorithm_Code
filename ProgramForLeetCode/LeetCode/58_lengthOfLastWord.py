class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==''or s==' ':
            return 0
        p=s.split(' ')
        r=0
        t=1
        while r==0:
            r=len(p[len(p)-t])
            if len(p)-t==0:
                return r
            t = t + 1
        return r

Solution().lengthOfLastWord("a ")
