class solution(object):
    def Sub_Pair(self,th,len_min,len_max,s1,s2):
        res=0
        for e in s1:
            if len(e)<len_min or len(e)>len_max:
                s1.remove(e)
        for e in s2:
            if len(e)<len_min or len(e)>len_max:
                s2.remove(e)
        if len(s1)>len(s2):
            ss1=s2
            ss2=s1
        else:
            ss1=s1
            ss2=s2
        for e in ss2:
            if e in ss1:
                res+=2
        return res
th=int(input())
len_min=int(input())
len_max=int(input())
s1=input().split(',')
s2=input().split(',')
print(solution().Sub_Pair(th,len_min,len_max,s1,s2))