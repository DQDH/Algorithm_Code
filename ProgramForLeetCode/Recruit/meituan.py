class solution(object):
    def Q1(self, data1, data2):
        memo = [[0] * (len(data2) + 1) for _ in range(len(data1) + 1)]
        for i in range(len(data1) - 1, -1, -1):
            for j in range(len(data2) - 1, -1, -1):
                if data1[i] == data2[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)
n1=int(input())
data1=list(map(int,input().split()))
n2=int(input())
data2=list(map(int,input().split()))
print(solution().Q1(data1,data2))