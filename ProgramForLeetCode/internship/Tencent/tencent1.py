def ques1(num1,num2):
    check_point = num1[0]
    start = num1[1]
    index = 1
    res = []
    while index<= check_point-1:
        ls = [0]*len(num2)
        ls = [abs(num2[i]-start) for i in range(len(num2))]
        min_val = min(ls)
        min_index=ls.index(min_val)
        res.append(min_val)
        start = num2[min_index]
        num2.pop(min_index)
        index += 1
    return sum(res)
num1 = [int(v) for v in input().split()]
num2 = [int(v) for v in input().split()]
res =ques1(num1,num2)
print(res)