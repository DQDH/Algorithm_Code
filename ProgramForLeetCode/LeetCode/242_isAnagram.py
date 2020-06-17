class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s={}
        dict_t={}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in dict_s:
                    dict_s[s[i]]=0
                else:
                    dict_s[s[i]]+=1
                if s[i] not in t:
                    return False
                if t[i] not in dict_t:
                    dict_t[t[i]]=0
                else:
                    dict_t[t[i]]+=1
        for value,key in enumerate(dict_s):
            if dict_s[key]!=dict_t[key]:
                return False
        return True