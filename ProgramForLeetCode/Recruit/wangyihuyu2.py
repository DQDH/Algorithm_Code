class solution(object):
    def compute(self,data):
        m,t,m1,t1,m2,t2=data[0],data[1],data[2],data[3],data[4],data[5]
        current_t1,current_t2,current_volume=0,0,0
        gei,pai=m1,m2
        for i in range(0,t):
            if (i//t1)%2==0:
                gei=m1
            else:
                gei=0
            if (i//t2)%2==0:
                pai=m2
            else:
                pai=0
            current_volume+=(gei-pai)
            if current_volume<=0:
                current_volume=0
            if current_volume>=m:
                current_volume=m
        return current_volume
# t = int(input())
t=1
for i in range(t):
    # nums = list(map(int, input().split()))
    nums=[10000,1000,10,5,5,3]
    print(solution().compute(nums))
# class solution(object):
#     def max_strs(self,strs):
#         n=len(strs)
#         tmp=0
#         l,h,res=0,0,0
#         for h in range(n):
#             if strs[h]!='N':
#                 tmp+=1
#             while tmp>2:
#                 if strs[l]=='N':
#                     tmp-=1
#                 l+=1
#             res=max(res,h-l+1)
#         return res
# t = int(input())
# for i in range(t):
#     strs = input()
#     print(solution().max_strs(strs))


    # NNTN
    # NNNNGGNNNN
    # NGNNNNGNNNNNNNNSNNNN