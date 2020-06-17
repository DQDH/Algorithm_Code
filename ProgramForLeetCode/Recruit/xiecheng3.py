class solution(object):
    def Q3(self,res, num, fg, i, cnt):
        if fg[0] == 0:
            return
        if sum(fg) == 2 and fg[0] == 1 and num[i][0] != -1:
            res.append(cnt + num[i][0])
            return

        for kk in range(n):
            if num[i][kk] != -1 and fg[kk] > 0:
                fg[i] -= 1
                self.Q3(res, num, fg, kk, cnt + num[i][kk])
                fg[i] += 1
        return

n = int(input())
m = int(input())
num = [[-1 for i in range(n)] for j in range(n)]

for k in range(m):
    i, j, d = [int(tmp) for tmp in input().split(' ')]
    num[i][j] = d
    num[j][i] = d
f = [1] * n
f[0] = 2
res = []
solution().Q3(res, num, f, 0, 0)
print(min(res))