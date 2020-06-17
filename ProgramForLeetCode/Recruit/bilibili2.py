class solution(object):
    def Q2(self,data):
        dic={}
        for e in data:
            if e[0] not in dic:
                dic[e[0]]=[e[1]]
            else:
                dic[e[0]].append(e[1])
        lens=0
        res=0
        for key,value in dic.items():
            if len(value)>=lens:
                lens=len(value)
                if key>res:
                    res=key
        return res
# n=int(input())
# data=[]
# for i in range(n):
#     data.append(list(map(int,input().split())))
# print(solution().Q2(data))
data=[ [33956,27538],
[79731,91415],
[25288,33956],
[33956,84925],
[79731,25288]]
print(solution().Q2(data))

# 33956 27538
# 79731 91415
# 25288 33956
# 33956 84925
# 79731 25288