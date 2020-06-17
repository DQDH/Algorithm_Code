def white_Black_matrix(m,n,matrix):
    res=0
    if m==1:
        for j in range(1,n-1):
            if matrix[m-1][j]==matrix[m-1][j-1]:
                res+=1
            if matrix[m-1][j-1]!=matrix[m-1][j+1]:
                matrix[m-1][j + 1]=matrix[m-1][j-1]
                res+=1
        return min(res,n-res)
    if n==1:
        for j in range(1,n-1):
            if matrix[j][n-1]==matrix[j-1][n-1]:
                res+=1
            if matrix[j-1][n-1]!=matrix[j+1][n-1]:
                matrix[j + 1][n-1]=matrix[j-1][n-1]
                res+=1
        return min(res,m-res)
    for i in range(m):
        for j in range(n):
            if matrix[i-1][j]:
                if matrix[i-1][j]!=matrix[i][j+1]:
                    matrix[i][j+1]=matrix[i-1][j]
                    res+=1
            if matrix[i][j-1]:
                if matrix[i][j - 1] != matrix[i + 1][j]:
                    matrix[i + 1][j]=matrix[i][j - 1]
                    res+=1
            if matrix[i][j+1]!=matrix[i+1][j]:
                matrix[i + 1][j]=matrix[i][j+1]
                res+=1
    return res
shape = [each for each in map(int, input().split())]
matrix=[]
for i in range(shape[0]):
    matrix.append([each for each in map(int, input().split())])
print(white_Black_matrix(shape[0],shape[1],matrix))