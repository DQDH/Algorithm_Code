#include <bits/stdc++.h>
#include<algorithm>
#include<cstdio>
#include <iostream>
using namespace std;
int main(){
    int M,N;
    cin>>N>>M;
    int nums[N];
    int oper[M][2];
    for (int i=0;i<N;i++){
        cin>>nums[i];
    }
    for (int i=0;i<M;i++){
        cin>>oper[i][0]>>oper[i][1];
    }
    for (int i=0;i<M;i++){
        if (oper[i][0]==1){
            sort(nums,nums+oper[i][1],less<int>());
        }
        else{
            sort(nums,nums+oper[i][1],greater<int>());
        }
    }
    for (int i=0;i<N-1;i++){
        cout<<nums[i]<<' ';
    }
    cout<<nums[N-1];
    return 0;
}