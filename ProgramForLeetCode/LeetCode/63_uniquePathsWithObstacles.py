class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        obstacleGrid[0][0]=1
        for i in range(1,m):
            obstacleGrid[i][0]=int(obstacleGrid[i][0]==0 and obstacleGrid[i-1][0]==1)
        for j in range(1,n):
            obstacleGrid[0][j]=int(obstacleGrid[0][j]==0 and obstacleGrid[0][j-1]==1)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                else:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]
print(Solution().uniquePathsWithObstacles([
  [0,1,0],
  [0,1,0],
  [0,0,0]
]))