class solution(object):
    def max_alike(self, s1, s2, x):
        res=[]
        for k in range(len(s1)):
            i=0
            r=0
            while i<x*len(s1):
                tmp=0
                for e in s1[k]:
                    if e in s2[i]:
                        tmp+=1
                Jaccard=tmp*1.0/(len(s1[k])+len(s2[i])-tmp)
                if Jaccard>r:
                    r=i
                i+=1
            res.append(r)
        return ','.join([str(i) for i in res])
s1 = input().split(',')
s2 = input().split(',')
x = int(input())
print(solution().max_alike(s1, s2, x))