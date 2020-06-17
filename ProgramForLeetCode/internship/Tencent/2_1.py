def Q3(n_k,num):
    n = n_k[0]
    k = n_k[1]
    res=[]
    num.sort()
    i=0
    while i<k:
        res.append(num[0])
        num1=[k-num[0] for k in num[1:]]
        num=[num[0]]+num1
        num.sort()
        i=i+1
    return res
n = input().split(' ')
n_k = [int(x) for x in n]
num = input().split(' ')
num = [int(y) for y in num]
res = Q3(n_k,num)
for l in res:
    print(l)
