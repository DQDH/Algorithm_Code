class solution(object):
    def IsValid(self,nums):
        data_i=[1,2,3,4,5]
        data=[]
        for i in range(5):
            data.append([i* 10+j for j in data_i])
        k=0
        while k<len(nums)-1:
            e=nums[k]
            row=e//10
            col=e%10-1
            neibor =[]
            if row>0:
                neibor.append(data[row-1][col])
            if row<4:
                neibor.append(data[row+1][col])
            if col>0:
                neibor.append(data[row][col-1])
            if col<4:
                neibor.append(data[row][col+1])
            else:
                if row<4:
                    neibor.append(data[row+1][0])
            k+=1
            if nums[k] not in neibor:
                return 0
        return 1
while True:
    try:
        print(solution().IsValid(list(map(int,input().split(' ')))))
    except:
        print(0)