class solution(object):
    def Q3(self,data,S):
        if not data:
            return -1
        if sum(data)<S:
            return -1
        C=[0]
        for e in data:
            if e>=S:
                return 1
            C.append(C[-1]+e)
        d=[]
        r=len(data)+1
        k=0
        for i,c in enumerate(C):
            while d and d[-1][0] >=c:
                d.pop()
            while k<len(d) and d[k][0]<c-S:
                k+=1
            if 0<=k-1<len(d) and i-d[k-1][1]<r:
                r=i-d[k-1][1]
            d.append((c,i))
        return -1 if r>len(data) else r

data1=list(map(int,input().split()))
N,S=data1[0],data1[1]
data=list(map(int,input().split()))
print(solution().Q3(data,S))