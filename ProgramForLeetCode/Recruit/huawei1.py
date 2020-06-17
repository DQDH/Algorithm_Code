class solution(object):
    def Q1(self,):
        return
nums=list(map(int,input().split()))
n=int(input())
print(solution().Q1())
'''
#include <iostream>
using namespace std;
int main(int arg,char *args[]){
    int res=0;
    int r;
    cin >> r;
    for (int i=1;i<r/3;i++){
        double j =r-(double) r*r/(2*r-2*i);
        if (i<j &&j-(int)j <1e-5){
            res++;
        }
    }
    cout <<res;
    return 0;
}

'''