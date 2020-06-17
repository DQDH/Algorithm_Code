s = input()
res = []
ptr = 0

for i in range(len(s)):
    ptr = max(ptr, s.rindex(s[i]))
    if i == ptr:
        res.append(ptr + 1 - sum(res))
        ptr = 0
    # print(res)

for x in res[:-1]:
    print(x, end=',')
print(res[-1])
# class solution(object):
#     def Q1(self,s):
#         if len(s) == 0:
#             return [0]
#         r=[]
#         tt = 0
#         while tt<len(s):
#             num=0
#             tmp=1
#             fix=s[tt]
#             for i in range(tt,len(s)):
#                 if s[i] ==fix:
#                     num=tmp
#                     tmp+=1
#                 else:
#                     tmp+=1
#             tt+=num
#             r.append(num)
#         return r
# for i in range(100):
#     s = input()
#     res=solution().Q1(s)
#     print(','.join([str(e) for e in res]))