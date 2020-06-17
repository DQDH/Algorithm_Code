def move(s):
    if '\r' in s:
        s=s[:-1]
    if len(s)<2:
        return s
    ls=len(s)
    i=0
    while i<ls:
        if s[i].isupper():
            s=s[:i]+s[i+1:]+s[i]
            ls=ls-1
        else:
            i=i+1
    return s
try:
    while True:
        s=input()
        print(move(s))
except:
    pass
