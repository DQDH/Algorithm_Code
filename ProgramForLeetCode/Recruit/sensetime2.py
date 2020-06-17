class Solution(object):
    def Q2(self,n,m,sweet,all):
        Max_n=float('inf')
        s=-1
        for e in all:
            if  n<1:
                print(-1)
            nn=0
            num=-1
            for nnn in sweet[e[0]-1:e[1]]:
                if nnn!=Max_n and nnn>num:
                    nn+=1
                    num=nnn
            if e[2]>=nn and s==-1:
                print(num)
                # print(max(sweet[e[0]-1:e[1]]))
                sweet[e[0]-1:e[1]]=[Max_n]*(e[1]-e[0]+1)
            else:
                k=0
                while k<e[2]:
                    Min=min(sweet[e[0]-1:e[1]])
                    for i in range(e[0]-1,e[1]):
                        if sweet[i]==Min:
                            k+=1
                            if k==e[2]:
                                print(sweet[i])
                                sweet[i]=Max_n
                                break
                            else:
                                sweet[i]=Max_n
data=list(map(int,input().split()))
n,m=data[0],data[1]
sweet=list(map(int,input().split()))
all=[]
for i in range(m):
    all.append(list(map(int,input().split())))
Solution().Q2(n,m,sweet,all)