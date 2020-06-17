def Ep(m,n,max):
    E=1
    if n!=1:
        for i in range(1,max):
            E+=(1.0/m)*Ep(m,n-1,max)
        for j in range(max,m):
            E+=(1.0/m)*Ep(m,n-1,j)
    else:
        for i in range(1,max):
            E+=(1.0/m)*max
        for j in range(max,m):
            E+=(1.0/m)*j
    return E
n=int(input())
ls=list(map(int,input().split(' ')))
m=max(ls)
print(Ep(n,m,1))