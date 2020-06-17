class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sa=s.lower()
        ss=''
        for si in sa:
            if si !=' 'and si.isalnum():
                ss=ss+si
        for i in range(len(ss)//2):
            if ss[i]!=ss[len(ss)-i-1]:
                return False
        return True
Solution().isPalindrome("A man, a plan, a canal: Panama")