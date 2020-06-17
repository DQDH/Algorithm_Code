def class_N_string(N,strs):
    res=0
    dict={}
    for i in range(N):
        length=len(strs[i])
        if length not in dict:
            dict[length]=[''.join(sorted(strs[i]))]
        else:
            flag=1
            tmp=''.join(sorted(strs[i]))
            for j in dict[length]:
                if j==tmp:
                    flag=0
                    break
            if flag==1:
                dict[length].append(tmp)
    for key in dict:
        res+=len(dict[key])
    return res
# N=int(input())
# strs=[]
# for i in range(N):
#     strs.append(input())
# print(class_N_string(N,strs))

def class_N_string1(N,strs):
    res=0
    dict={}
    for i in range(N):
        length=len(strs[i])
        if length not in dict:
            dict[length]=[strs[i]]
        else:
            flag=1
            for j in dict[length]:
                if sorted(j)==sorted(strs[i]):
                    flag=0
                    break
            if flag==1:
                dict[length].append(strs[i])
    for key in dict:
        for value in dict[key]:
            res+=1
    return res
N = 4
strs = ['abcd','abac','aabc','bacd']
print(class_N_string1(N, strs))