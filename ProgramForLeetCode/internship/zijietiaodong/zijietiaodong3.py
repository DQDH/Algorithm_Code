n = input()
a_all=[]
all_reward=0
# while True:
#     a_all.append(1)
for i in range(1,int(n)):
    if a_all[i]>a_all[i-1] and a_all[i]>a_all[(i+1)%(len(a_all))]:
        all_reward+=3
    elif a_all[i]>a_all[i-1] and a_all[i]<=a_all[(i+1)%(len(a_all))]:
        all_reward+=2
    elif a_all[i]>=a_all[i-1] and a_all[i]<a_all[(i+1)%(len(a_all))]:
        all_reward+=2
    elif a_all[i]<=a_all[i-1] and a_all[i]>a_all[(i+1)%(len(a_all))]:
        all_reward+=2
    elif a_all[i]<a_all[i-1] and a_all[i]>=a_all[(i+1)%(len(a_all))]:
        all_reward+=2
    elif a_all[i] > a_all[i - 1] and a_all[i] < a_all[(i+1)%(len(a_all))]:
        all_reward +=1
    else:
        pass

print(all_reward)

# def resp(a, A):
#     if a==1:
#         return 1
#     if a== 2:
#         if A[0]==A[1]:
#             return 2
#         else:
#             return 3
#     if a>2:
#         max_index = A.index(max(A))
#         max_num = max(A)
#         sum_money = 0
#         m = max_num
#         if A[max_index]>A[max_index-1] and A[max_index]>A[max_index+1]:
#             sum_money += m
#         money = [0]*a
#         for i in range(max_index, (max_index - a), -1):
#             if (A[i] > A[i - 1] and A[i - 1] > A[i - 2]):
#                 m -= 1
#                 sum_money += m
#                 money[i-1] = m
#             elif (A[i] > A[i - 1] and A[i - 1] <= A[i - 2]):
#                 m = 1
#                 sum_money += m
#                 money[i-1] = m
#             elif A[i] < A[i - 1]:
#                 m += 1
#                 sum_money += m
#                 money[i - 1] = m
#             elif A[i] == A[i-1]:
#                 if A[i-1]>A[i-2]:
#                     m = money[i-2]+1
#                     sum_money += m
#                     money[i - 1] = m
#                 elif A[i-1]==A[i-2]:
#                     m = money[i - 2]
#                     money[i - 1] = m
#         return sum_money
#
# for i in range(n):
#     a = int(a2)
#     A = list(map(int, A2.split()))
#     print(resp(a, A))