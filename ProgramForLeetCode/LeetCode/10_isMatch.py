class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s)<2 and s in p:
            return True
        if (len(s)!=len(p)) and ('*' not in p):
            return False
        if '.*' in p:
            kk=p.index('.*')
            if s[:kk]==p[:kk]:
                return True
        length=len(s)
        if p[0]=='.':
            p=s[0]+p[1:]
        for i in range(1,length):
            if '*' not in p:
                if len(p)!=len(s):
                    return False
            if s[i]!=p[i]:
                if p[i]=='*':
                    if s[i]!=s[i-1]:
                        return False
                    else:
                        if i+1<len(p) and i+1<len(s):
                            if s[i+1]==p[i+1]:
                                p=p[:i]+s[i]+p[i+1:]
                        else:
                            p=p[:i]+s[i]+'*'+p[i+1:]
                elif p[i] == '.':
                    p=p[:i]+s[i]+p[i+1:]
                # else:
                #     return False
        return s in p
print(Solution().isMatch("aab","c*a*b"))