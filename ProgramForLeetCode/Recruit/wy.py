def find_small(s):
    for i in range(1,len(s)):
        for j in range(0,i):
            if s[i]+s[j]<s[j]+s[i]:
                s[i],s[j]=s[j],s[i]
        return s
def solution():
    n=int(input())
    s=input().split()
    tmp=[]
    out=[]
    for i in s:
        tt=int(i)
        if tt%2==0:
            out.append(tt)
        else:
            tmp.append(tt)
    if len(tmp)==n:
        return tmp
    if len(out)==n:
        return out
    return(find_small(s))
data=solution()
res=''
for e in data:
    res+=str(e)+''
print(res)