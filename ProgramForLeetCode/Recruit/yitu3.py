st = input().split(' ')
m = int(st[0])
k = int(st[1])
st = input().split(' ')
def Q2(st,k):
    th_one = []
    th_two = []
    cnt = 0
    for ss in st:
        if int(ss) % 3 != 0:
            if int(ss) % 3 == 1:
                th_one.append(1)
            else:
                th_two.append(2)
        else:
            cnt += 1
    x = min(len(th_one), len(th_two))
    if x >= k:
        cnt += k
    else:
        cnt += x
        k -= x

        k_2 = int((max(len(th_one), len(th_two)) - x) / 3)
        if (k_2 * 2) >= k:
            cnt += int(k / 2)
        else:
            cnt += k_2
    return cnt
print(Q2(st,k))