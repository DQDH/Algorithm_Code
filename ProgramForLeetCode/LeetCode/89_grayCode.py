class Solution(object):
    def grayCode(self, n):
        if n<=1:
            return [k for k in range(n+1)]
        """
        :type n: int
        :rtype: List[int]
        """
        res=['0','1']
        i=1
        while i<n:
            res_t=[]
            for m in range(len(res)):
                res_t.append('0'+res[m])
            for k in range(len(res)-1,-1,-1):
                res_t.append('1'+res[k])
            res=res_t
            i+=1
        res=[int(res_ii,base=2) for res_ii in res]
        return res
print(Solution().grayCode(2))