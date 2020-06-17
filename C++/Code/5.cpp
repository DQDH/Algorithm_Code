#include<iostream>
#include<queue>
#include<memory>
#include<cstring>
using namespace std;
int all[10000000];
int sp=0;
void fun(int n,int m){
    queue<int> q;
    q.push(n-1);
    q.push(n*2);
    q.push(n*3);
    while (!q.empty)
    {
        int n=q.size();
        for(int i=0;i<n;i++){
            int v=q.front();
            q.pop();
            if( all[v]==1 or v<0 or v>3*m){
                continue;
            }
            if(v==m){
                sp++;
                return;
            }
            q.push(v-1);
            q.push(v*2);
            q.push(v*3);
            all[v]=1;
        }
        sp++;
    }
    
}
int main(){
    int n;cin>>n;
    if (n==1){
        cout<<0<<endl;return 0;
    }
    memset(all,0,sizeof(all));
    all[1]=1;
    fun(1,n);
    cout<<sp<<endl;
    return 0;
}


// void sort_less(int nums[],int x){
//     for(int )
// }
// void sort_grerater(int nums[],int x){
    
// }