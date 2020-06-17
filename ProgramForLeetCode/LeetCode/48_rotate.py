class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n//2):
            matrix[i],matrix[n-1-i]=matrix[n-1-i],matrix[i]
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i], matrix[i][j]
        return matrix
print(Solution().rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))