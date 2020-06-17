N = int(input())
a = input().split(' ')
b = input().split(' ')
ai=[]
bi=[]
for i in range(N):
    ai.append(int(a[i]))
    bi.append(int(b[i]))
def Q1(ai,bi):
    total = 0
    for indexb, bb in enumerate(bi):
        if bb == 0:
            continue
        for indexa, aa in enumerate(ai):
            if bb == aa:
                total += (indexb - indexa) * aa
                bi[indexb] = 0
                ai[indexa] = 0
                break
            if bb > aa:
                total += (indexb - indexa) * aa
                bb = bb - aa
                bi[indexb] = bb - aa
                ai[indexa] = 0
                continue
            if bb < aa:
                total += (indexb - indexa) * bb
                ai[indexa] = aa - bb
                bi[indexb] = 0
                break
    return total
print(Q1(ai,bi))