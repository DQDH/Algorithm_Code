def Fibonancci(k):
    if k==0:
        return 0
    elif k==1:
        return 1
    else:
        return Fibonancci(k-1)+Fibonancci(k-2)
def Fibonancci1(k):
    tmp_nums=[0,1]
    if k<2:
        return tmp_nums[k]
    else:
        while k>1:
            tmp=tmp_nums[1]
            tmp_nums[1]=tmp_nums[0]+tmp_nums[1]
            tmp_nums[0]=tmp
            k-=1
    return tmp_nums[1]
print(Fibonancci1(6))