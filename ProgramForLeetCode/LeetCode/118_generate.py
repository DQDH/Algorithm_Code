class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        r=[[1],[1,1]]
        for n in range(3,numRows+1):
            t=[]
            t.append(1)
            for i in range(n-2):
                t.append(r[n-2][i]+r[n-2][i+1])
            t.append(1)
            r.append(t)
        return r
Solution().generate(5)