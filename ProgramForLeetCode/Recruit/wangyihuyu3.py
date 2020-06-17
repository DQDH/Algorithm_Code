class solution(object):
    def max_strs(self,strs):
        sl=0
        begin=0
        nums=0
        max_=0
        for i in range(len(strs)):
            sl+=1
            if nums<2:
                if strs[i]!='N':
                    nums+=1
            elif nums==2:
                if strs[i]!='N':
                    while strs[begin]=='N':
                        begin+=1
                        sl-=1
                    begin+=1
                    sl-=1
            max_=max(max_,sl)
        return max_
t = int(input())
for i in range(t):
    strs = input()
    print(solution().max_strs(strs))


    # NNTN
    # NNNNGGNNNN
    # NGNNNNGNNNNNNNNSNNNN