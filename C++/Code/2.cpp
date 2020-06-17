#include <bits/stdc++.h>
#define ll long long int

using namespace std;
int N=1000005;
int k[1000005];
void fa(){
    memset(k,0,sizeof(k));
    k[0]=k[1]=0;
    for(int i=2;i<N;i++){
        if(i%2==0){
            k[i]=i/4*2+k[i-2];
        }else{
            k[i]=(i+1)/4+k[i-1]-1;
        }
    }
}
int main(){
    int n;
    fa();
    scanf("%d",&n);
    while(n--){
        int x;
        scanf("%d",&x);
        for(int i=0;i<N;i++){
        if(k[i]>=x){
            printf("%d\n",i);
            break;
            }
        }
    }
    return 0;
}