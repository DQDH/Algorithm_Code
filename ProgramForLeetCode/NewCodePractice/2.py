'''
https://www.nowcoder.com/profile/334972052/test/25652547/224353#summary
小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，
所以希望你在老师讲到有趣的部分的时候叫醒他一下。你知道了小易对一堂课每分钟知识点的感兴趣程度，
并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，这会使得他在接下来的k分钟内保
持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。
'''

class solution(object):
  def max_value(self,n,k,num,flags):
    sleep_value=0
    clear=0
    for i in range(n):
      if flags[i] == 1:
        clear += num[i]
    for i in range(n):
      if flags[i]==0:
        if i + k > n and flags[i - 1] == 0:
          break
        tmp=0
        edge=min(n,i+k)
        for j in range(i,edge):
          if flags[j]==0:
            tmp+=num[j]
      sleep_value=max(tmp,sleep_value)
    return sleep_value+clear
input_1=[e for e in map(int,input().split())]
n,k=input_1[0],input_1[1]
num=[e for e in map(int,input().split())]
flags=[e for e in map(int,input().split())]
print(solution().max_value(n,k,num,flags))
