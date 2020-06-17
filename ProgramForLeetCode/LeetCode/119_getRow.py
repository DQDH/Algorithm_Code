class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        t=[1,1]
        for n in range(2,rowIndex+1):
            r=[]
            r.append(1)
            for i in range(n-1):
                r.append(t[i]+t[i+1])
            r.append(1)
            t=r
        return r
Solution().getRow(3)