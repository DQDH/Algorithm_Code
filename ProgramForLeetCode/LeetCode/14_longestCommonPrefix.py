class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        l=len(strs[0])
        s=strs[0]
        for i in range(len(strs)):
            if strs[i]=="":
                return ""
            if len(strs[i])<l:
                l=len(strs[i])
                s=strs[i]
        for i in range(len(s)):
            for j in range(len(strs)):
                if strs[j][i]!=s[i]:
                    return s[0:i]
        return s