class solution(object):
    def Q1(self,data):
        d={}
        for dt in data:
            if dt in d.keys():
                d[dt] += 1
            else:
                d[dt] = 1
        m = max(d.values())
        if m > len(data) / 2:
            print("NO")
        else:
            print("YES")
n=int(input())
for i in range(n):
    n = input()
    st = [int(t) for t in input().split(" ")]
    solution().Q1(st)


