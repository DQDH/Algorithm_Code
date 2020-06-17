class Solution(object):
    def str_sort(self,s=''):
        if len(s) <= 1:
            return [s]
        str_list = []
        for i in range(len(s)):
            for j in self.str_sort(s[0:i] + s[i + 1:]):
                str_list.append(s[i] + j)
        return str_list
    def GetLocation(self,strs, n):
        c=list(set(strs))
        all=self.str_sort(''.join(c))
        for pp in all:
            N=0
            c=list(pp)
            for p in c:
                i=0
                while i<len(strs):
                    j=i
                    num=0
                    while j<len(strs) and strs[j]==p:
                        num+=1
                        j+=1
                    if num>1:
                        print(strs[i],i+num)
                        strs=strs[i+num:]
                        N+=1
                    else:
                        i+=1
                    if len(list(set(strs)))==len(strs):
                        for e in strs:
                            print(e,0)
                            print(e,0)
                            N+=2
                        i=len(strs)
            if N<n+1:
                break
strs = input()
n=int(input())
Solution().GetLocation(strs,n)