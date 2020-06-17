class solution(object):
    def Q4(self,n,nums):
        res = []
        for i in range(n):
            nu=2
            r=[]
            while nu <=nums[i]:
                if nums[i] % nu == 0:
                    r.append(nu)
                nu += 1
            res.append(r)
        print(res)
        tmp=[]
        for e in res:
            tmp+=e
        tmp=list(set(tmp))
        print(tmp)
        rrr={}
        for e in tmp:
            rrr[e]=0
            for r in res:
                if e in r:
                    rrr[e]+=1
        rst=1
        print(rrr)
        for key,value in rrr.items():
            if value>rst:
                rst=value
        return rst
# n=int(input())
# nums=list(map(int,input().split()))
# print(solution().Q4(n,nums))
n=5
nums=[1,2,3,7,14]
print(solution().Q4(n,nums))