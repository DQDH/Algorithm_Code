class solution(object):
    def auc_func(self,l,p):
     two_list = list(zip(p,l))
     rank = [values2 for values1,values2 in sorted(two_list,key=lambda x:x[0])]
     st = [i+1 for i in range(len(rank)) if rank[i]==1]
     tp,fp = 0,0
     for i in range(len(l)):
      if(l[i]==1):
       tp+=1
      else:
       fp+=1
     auc = (sum(st)- (tp*(tp+1))/2)/(tp*fp)
     return auc

n = int(input())
l = []
p = []
for i in range(n):
    s = input().split(' ')
    l.append(int(s[0]))
    p.append(float(s[1]))
print(solution().auc_func(l,p))