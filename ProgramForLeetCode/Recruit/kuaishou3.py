def Q3(n):
    res=0
    all=[-1 for i in range(n)]
    for i in range(2,n):
        if all[i]==-1:
            all[i]=1
        j=i
        while i*j<n:
            all[i*j]=-2
            j+=1
    all=all[2:]
    for i in range(n-2):
        if all[i]==-2:
            j=2
            while (i+2)%j!=0:
                j+=1
            all[i]=all[j-2]+all[(i+2)//j-2]
        res+=all[i]
    return res
print(Q3(int(input())))