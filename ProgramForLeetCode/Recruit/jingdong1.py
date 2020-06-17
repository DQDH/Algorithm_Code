class solution(object):
    def get_min_num(self,data):
        data_ = [[0 for x in range(5)] for y in range(5)]
        for i in range(5):
            for j in range(5):
                data_[i][j]=data[i][j]
        N=0
        while N>10:
            N+=1
            for n in range(1, 4):
                for i in range(5):
                    for j in range(5):
                        if data[i][j] == n:
                            num = 1
                            index_l = []
                            index_l.append([i, j])
                            if i - 1 >= 0 and data[i - 1][j] == n:
                                num += 1
                                index_l.append([i - 1, j])
                            if i + 1 < 5 and data[i + 1][j] == n:
                                num += 1
                                index_l.append([i + 1, j])
                            if j - 1 >= 0 and data[i][j - 1] == n:
                                num += 1
                                index_l.append([i, j - 1])
                            if j + 1 < 5 and data[i][j + 1] == n:
                                num += 1
                                index_l.append([i, j + 1])
                            if num > 2:
                                for ee in index_l:
                                    data_[ee[0]][ee[1]] = None
                        else:
                            continue
            for i in range(5):
                for j in range(5):
                    if data_[i][j]:
                        while i+1<5:
                            i+=1
                            if not data_[i][j]:
                                data_[i][j]=data_[i-1][j]
                                data_[i-1][j]=None
            data=data_
        res=0
        for i in range(5):
            for j in range(5):
                if data_[i][j]:
                    res+=1
        return res
# data=[]
# for i in range(5):
#     data.append(list(map(int,input().split())))
data=[[3,1,2,1,1],
[1,1,1,1,3],
[1,1,1,1,1],
[1,1,1,1,1],
[3,1,2,2,2]]
print(solution().get_min_num(data))