def same(n,strs1,strs2):
    l1=len(strs1)
    l2=len(strs2)
    data=[[0 for i in range(l2+1)] for j in range(l1+1)]
    for i in range(l1):
        for j in range(l2):
            if strs1[i]==strs2[j]:
                data[i+1][j+1]=data[i][j]+1
            elif data[i+1][j]>data[i][j+1]:
                data[i+1][j+1]=data[i+1][j]
            else:
                data[i+1][j]=data[i][j+1]
    return n-data[-1][-1]
n=int(input())
strs1=list(map(int,input().split(' ')))
strs2=list(map(int,input().split(' ')))
print(same(n,strs1,strs2))