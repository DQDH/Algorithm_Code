def reverse(s):
    res=''
    s = s[:-1]
    strs=s.split(' ')
    for s in strs[::-1]:
        if s!='':
            res = res+s+' '
    res = res[:-1]+'.'
    return res
print(reverse(input()))
