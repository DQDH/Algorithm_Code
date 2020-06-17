def Q1(strs):
    length=len(strs)
    for i in range(1,length+1):
        if length%i==0:
            if strs[:i] * (length // i) == strs:
                return i
a='ababc'
print(Q1(a))