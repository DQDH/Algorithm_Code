#include <bits/stdc++.h>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include <iostream>
using namespace std;
int main(){
    int H,W,K_H,K_W,S_H,S_W;
    cin>>H>>W;
    cin>>K_H>>K_W;
    cin>>S_H>>S_W;
    int nums[H][W];
    for (int i=0;i<H;i++){
        for(int j=0;j<W;j++){
            cin>>nums[i][j];
        }
    }
    int r[int((H-K_H)/S_H+1)][int((W-K_W)/S_W+1)];
    int p=0;int q=0;
    for (int i=0;i<H;i+=S_H){
        for(int j=0;j<W;j+=S_W){
            int res=0;
            for (int m=0;m<K_H;m++){
                for (int n=0;n<K_W;n++){
                    if(nums[i+m][j+n]>res){
                        res=nums[i+m][j+n];
                    }
                }
            }
            r[p][q]=res;
            q++;
        }
        p++;
        q=0;
    }
    for (int i=0;i<int((H-K_H)/S_H+1);i++){
        for (int j=0;j<int((W-K_W)/S_W+1);j++){
            cout<<r[i][j]<<' ';
        }
        cout<<endl;
    }
}