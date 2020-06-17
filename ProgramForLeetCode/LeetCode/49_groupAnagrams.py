class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict={}
        res=[]
        for str in strs:
            str1="".join(sorted(str))
            if str1 in dict:
                dict[str1].append(str)
            else:
                dict[str1]=[]
                dict[str1].append(str)
        for key in dict:
            res.append(dict[key])
        return res
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))