#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main(){
    int N,X,Y;
    cin>>N>>X>>Y;
    int nums[N];
    int res[N];
    int flag=0;
    for (int i=0;i<N;i++){
        res[i]=-1;
    }
    for (int i=0;i<N;i++){
        cin>>nums[i];
    }
    for (int i=0;i<N;i++){
        for (int j=i+1;j<N;j++){
            if (nums[i]+nums[j]==X and nums[i]==-1 and nums[j]==-1){
                res[i]=X;
                res[j]=X;
                flag=1;
            }
            if (nums[i]+nums[j]==Y and nums[i]==-1 and nums[j]==-1){
                res[i]=Y;
                res[j]=Y;
            }
        }
    }
    if (flag==1){
        cout<<"YES";
        for(int i=0;i<N;i++){
            cout<<res[i]<<' ';
        }
    }
    else{
        cout<<"NO";
    }
        
}



// #include <string.h>
// #include <vector>
// #include <iostream>
// using namespace std;
 
// int main()
// {
//     vector<int>obj;//创建一个向量存储容器 int
//     for(int i=0;i<10;i++) // push_back(elem)在数组最后添加数据 
//     {
//         obj.push_back(i);
//         cout<<obj[i]<<",";    
//     }
 
//     for(int i=0;i<5;i++)//去掉数组最后一个数据 
//     {
//         obj.pop_back();
//     }
 
//     cout<<"\n"<<endl;
 
//     for(int i=0;i<obj.size();i++)//size()容器中实际数据个数 
//     {
//         cout<<obj[i]<<",";
//     }
 
//     return 0;
// }