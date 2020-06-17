class solution(object):
    def tmp(self, num, k):
        res = 1
        for i in range(k):
            res = res * num
            num -= 1
        return res

    def Q2(self, k, nums, a, b):
        res = 0
        d = {}
        for n in range(a, b + 1):
            wf_n = n // k
            for i in range(1, wf_n + 1):
                wf = i
                rf = n - wf * k
                kk = min(wf, rf)
                res += self.tmp(wf + rf, kk) / (self.tmp(kk, kk))
            else:
                res += 1
            d[n] = res
        d[a-1]=0
        for e in nums:
            a, b = e[0], e[1]
            rrr = int(d[b] - d[a - 1])
            if rrr > 10 ** 9 + 7:
                print(rrr % (10 ** 9 + 7))
            else:
                print(rrr)
data = list(map(int, input().split(' ')))
N, k = data[0], data[1]
all = []
max_a, max_b = 0, 0
for i in range(N):
    all.append(list(map(int, input().split(' '))))
    if i == 0:
        max_a, max_b = all[i][0], all[i][1]
    else:
        max_a = min(all[i][0], max_a)
        max_b = max(all[i][1], max_b)
solution().Q2(k, all, max_a, max_b)