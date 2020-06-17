class solution(object):
    def Q3(self,n,data):
        nums=[]
        for i in range(n):
            for j in range(n):
                if i<j:
                    if data[i][j]>=3:
                        nums.append([i,j])
        # print(nums)
        res=[nums[0]]
        for e in nums[1:]:
            for r in res:
                if e[0] in r:
                    r.append(e[1])
        print(res)
        rst=len(res)
        rrr=[]
        for e in res:
            rrr+=e
        for i in range(n):
            if i not in rrr:
                rst+=1
        return rst
# n=int(input())
# data=[]
# for i in range(n):
#     data.append(list(map(int,input().split())))
n=3
data=[[0,4,0],
      [4,0,0],
      [0,0,0]]
print(solution().Q3(n,data))