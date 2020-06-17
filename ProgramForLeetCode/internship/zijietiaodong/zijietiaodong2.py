def Q2(s):
    i=0
    while i<len(s):
        if len(s[i:])>2:
            if s[i]==s[i+1] and s[i+1]==s[i+2]:
                s=s[:i+2]+s[i+3:]
                i=i-1
        if len(s[i:]) > 3:
            if s[i] == s[i + 1] and s[i + 2] == s[i + 3]:
                s = s[:i + 3] + s[i + 4:]
                i=i-1
        i=i+1
    s=s+s[i:]
    return s
n=int(input())
for i in range(n):
    print(Q2(input()))
# strs=['helloo','wooooooow']
