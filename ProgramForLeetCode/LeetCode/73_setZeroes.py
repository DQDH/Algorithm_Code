class Solution(object):
    def setZeroes(self, matrix):
        index = []
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                index.extend([j for j, x in enumerate(matrix[i]) if x == 0])
                matrix[i] = [0 for m in range(len(matrix[i]))]
        for i in range(len(matrix)):
            for j in index:
                matrix[i][j] = 0
        return matrix
    def setZeroes1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        index=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    index.append([i,j])
        for index_i in index:
            matrix[index_i[0]]=[0]*n
            for k in range(m):
                matrix[k][index_i[1]]=0
        return matrix
print(Solution().setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))