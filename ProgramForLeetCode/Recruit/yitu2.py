# class solution(object):
#     def get_max_value(self,N,M,S,D,Qi,data):
#         print(data)
#         edges = [[1000 for x in range(N)] for y in range(N)]
#         for e in data:
#             tmp=edges[e[0]-1]
#             tmp[e[1]-1]=e[2]
#         print(edges)
#         dis={}
#         for i in range(N):
#             if i!=S:
#                 dis[i]=edges[S-1][i]
#         visited = []
#         min_dis = None
#         min_dis_point = None
#         for i in range(len(dis)):
#             sort_dis = sorted(dis.items(), key=lambda item: item[1])
#             # 找到dis中距离起始点距离最小的点
#             for p, d in sort_dis:
#                 if p not in visited:
#                     min_dis_point = p
#                     min_dis = d
#                     visited.append(p)
#                     break
#             for j in range(len(edges)):
#                 # 权重小于1000的为相邻点
#                 if edges[min_dis_point - 1][j] < 1000:
#                     update = min_dis + edges[min_dis_point - 1][j]
#                     # 若经过min_dis_point到j的距离比起点直达j的距离大，则更新
#                     if dis[j] > update:
#                         dis[j] = update
#         print(dis)
#         return dis[D-1]
#
# # nums=list(map(int,input().split()))
# # N,M,S,D=nums[0],nums[1],nums[2],nums[3]
# # Qi=list(map(int,input().split()))
# # data=[]
# # for i in range(M):
# #     data.append(list(map(int,input().split())))
# # print(solution().get_max_value(N,M,S,D,Qi,data))
# N, M, S, D=4,5,1,4
# Qi=[10,20,30,40]
# data=[[1,2,2],
# [1,3,3],
# [2,3,2],
# [3,4,3],
# [2,4,4]]
# print(solution().get_max_value(N,M,S,D,Qi,data))
# import sys
# sys.setrecursionlimit(100000000)
N, M, S, D=4,5,1,4
Qi=[10,20,30,40]
datas=[[1,2,2],
[1,3,3],
[2,3,2],
[3,4,3],
[2,4,4]]
# nums=list(map(int,input().split()))
# N,M,S,D=nums[0],nums[1],nums[2],nums[3]
# Qi=list(map(int,input().split()))
# datas=[]
# for i in range(M):
#     datas.append(list(map(int,input().split())))
res=[]
def floyd(Qi):
    ttt=0
    n = len(graph)
    for k in range(n):
        i,j=S,D
        if graph[i][k] + graph[k][j] <= graph[i][j]:
            if Qi[i-1]+Qi[j-1]+Qi[k-1]>ttt and ttt!=0:
                graph[i][j] = graph[i][k] + graph[k][j]
                parents[i][j] = parents[k][j]  # 更新父结点
            else:
                ttt= Qi[i-1]+Qi[j-1]+Qi[k-1]
                graph[i][j] = graph[i][k] + graph[k][j]
                parents[i][j] = parents[k][j]  # 更新父结点
sum_=0
def print_path(i, j):
    if i != j:
        print_path(i, parents[i][j])
    res.append(j)
n = M
inf = 9999
graph = [[(lambda x: 0 if x[0] == x[1] else inf)([i, j]) for j in range(n)] for i in range(n)]
parents = [[i] * n for i in range(5)]
for u, v, c in datas:
    graph[u][v] = c
floyd(Qi)
print_path(S-1, D-1)
rr=0
for e in res:
    rr+=Qi[e]
print(graph[S][D],rr)