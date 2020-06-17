class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res=[[0]*n for k in range(n)]
        max_up,max_left=0,0
        max_down,max_right=n,n
        direction=0
        num=1
        while num<=n**2:
            if direction==0:
                for i in range(max_left,max_right):
                    res[max_up][i]=num
                    num+=1
                max_up+=1
            elif direction==1:
                for i in range(max_up,max_down):
                    res[i][max_right-1]=num
                    num+=1
                max_right-=1
            elif direction==2:
                for i in range(max_right-1,max_left-1,-1):
                    res[max_down-1][i]=num
                    num+=1
                max_down-=1
            else:
                for i in range(max_down-1,max_up-1,-1):
                    res[i][max_left]=num
                    num+=1
                max_left+=1
            direction=(direction+1)%4
        return res
print(Solution().generateMatrix(3))