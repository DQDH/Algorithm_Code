def q4(tls,max_num):
    c=[0 for _ in range(max_num)]
    for num in tls:
        c[num]+=1
    tls.clear()
    for i in range(max_num):
        for j in range(c[i]):
            tls.append(i)
    return tls

    # n,m=len(nums),len(nums[0])
    # l,h=nums[0][0],nums[n-1][m-1]
    # while l<h:
    #     c=0
    #     mid=l+(h-l)//2
    #     for i in range(n):
    #         j =m-1
    #         while j>=0 and nums[i][j]>mid:
    #             j-=1
    #         c+=j+1
    #     if c>=k:
    #         h=mid
    #     else:
    #         l=mid+1
    # return l
n, m, k = list(map(int, input().split(' ')))
nums = []
for i in range(n):
    # nums.append([])
    for j in range(m):
        nums[i].append((i + 1) * (j + 1))
print(q4(nums, n * m + 1 - k))
    # if len(nums)==0:
    #     return []
    # l=[a for a in nums[1:] if a>nums[0]]
    # r=[a for a in nums[1:] if a<nums[0]]
    # if len(l)>k:
    #     return q4(l,k)
    # elif len(l)==k:
    #     return l
    # elif len(l)+1==k:
    #     return l+[nums[0]]
    # else:
    #     return l+[nums[0]]+q4(r,k-1-len(l))
    #2
    # l=0
    # r=len(nums)-1
    # while l<r:
    #     cur =l
    #     nums[(l+r)//2],nums[r]=nums[r],nums[(l+r)//2]
    #     for i in range(l,r):
    #         if nums[i]<nums[r]:
    #             nums[cur],nums[i]=nums[i],nums[cur]
    #             cur+=1
    #     nums[cur],nums[r]=nums[r],nums[cur]
    #     if cur==len(nums)-k:
    #         return  nums[cur]
    #     elif cur<len(nums)-k:
    #         l=cur+1
    #     else:
    #         r=cur-1

#1
#     rt=sorted(nums,reverse=True)
#     return rt[k-1]
# n,m,k=list(map(int,input().split(' ')))
# nums=[]
# for i in range(m):
#     for j in range(n):
#         nums.append((i+1)*(j+1))
# print(q4(nums,k))
'''
#include "stdio.h"
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
vector<vector <int>> *ma
'''