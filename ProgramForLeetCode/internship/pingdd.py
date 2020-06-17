def two_sum(n,num1,num2):
    num1=sorted(num1)
    num2=sorted(num2)
    num1.reverse()
    res1=0
    res2=0
    for i in range(n):
        res1=num1[i]*num2[i]+res1
    num1.reverse()
    num2.reverse()
    for j in range(n):
        res2=num1[i]*num2[i]+res2
    return min(res1,res2)
a=two_sum(3,[1,1,3],[10,30,20])

####
def delete(str):
    str=str.lower()
    l=list(str)
    ll=len(l)
    i=0
    while i<ll:
        if l[i] in l[i+1:]:
            del(l[i])
            ll=ll-1
        i=i+1
    return l[0]
a=delete('AxBAXY')
print(a)

#ykq
import sys
if __name__ == "__main__":
    strList = []
    for line in sys.stdin:  #当没有接受到输入结束信号就一直遍历每一行
        tempStr = line.split()#对字符串利用空字符进行切片
        strList.extend(tempStr)
#guanwang
import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print(int(lines[0]) + int(lines[1]))
except:
    pass