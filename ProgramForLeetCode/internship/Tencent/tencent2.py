def Q2(n,num):
    if n<4:
        return min(num)
    res=0
    i=0
    while i<n+3:
        if n-i<3:
            return res
        if sum(num[i:i+2])>num[i+2]:
            res=res+num[i+2]
            i=i+3
        else:
            if num[i]<num[i+1]:
                res=res+num[i]
                i=i+1
            if num[i]>=num[i+1]:
                res=res+num[i+1]
                i=i+2
    return res
if __name__ == "__main__":
    # n = int(input())
    # list = []
    # for i in range(n):
    #     num = [int(n) for n in input().split()]
    #     list.append(num)
    a=Q2(4,[3,1,8,4])
    print(a)
