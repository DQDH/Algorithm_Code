class solution(object):
    def Q1(self,data,N):
        data=sorted(data,reverse=True)
        ji=[]
        ou=[]
        for k in range(len(data)):
            if data[k]%2==0:
                ou.append(data[k])
            else:
                ji.append(data[k])
        if len(ou)<=N:
            return ','.join([str(i) for i in ou[:N]])
        else:
            res=ou+ji[:N-len(ou)]
            return ','.join([str(i) for i in res])
data=input().split(';')
N=int(data[1])
nums= list(map(int,data[0].split(',')))
print(solution().Q1(nums,N))

'''
class solution(object):
    def Q1(self, data, N):
        odd = []
        even = []
        for num in data:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        even = sorted(even, reverse=True)
        odd = sorted(odd, reverse=True)
        data.clear()
        data=even+odd
        data=data[:N]
        return ','.join([str(i) for i in data])
data=input().split(';')
N=int(data[1])
nums= list(map(int,data[0].split(',')))
print(solution().Q1(nums,N))
'''