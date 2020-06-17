n1 = input()
n2 = input()
for i in range(int(input())):
    l, r = list(map(int, input().split()))
    print(n1[l-1: r].count(n2))
