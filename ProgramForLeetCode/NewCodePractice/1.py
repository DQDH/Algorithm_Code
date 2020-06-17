'''
https://www.nowcoder.com/profile/334972052/test/25652547/224352#summary
小易有一个古老的游戏机，上面有着经典的游戏俄罗斯方块。因为它比较古老，所以规则和一般的俄罗斯方块不同。
荧幕上一共有 n 列，每次都会有一个 1 x 1 的方块随机落下，在同一列中，后落下的方块会叠在先前的方块之上，当一整行方块都被占满时，这一行会被消去，并得到1分。
有一天，小易又开了一局游戏，当玩到第 m 个方块落下时他觉得太无聊就关掉了，小易希望你告诉他这局游戏他获得的分数。
'''
class solution(object):
  def get_score(self,m,n,num):
    cols={}
    for e in num:
      if e in cols:
        cols[e]+=1
      else:
        cols[e]=1
    if len(cols)<n:
      return 0
    res=m//n
    for k,v in cols.items():
      res=min(res,v)
    return res
input_1=[each for each in map(int,input().split())]
n=input_1[0]
m=input_1[1]
input_2=[each for each in map(int,input().split())]
print(solution().get_score(m,n,input_2))