#include <bits/stdc++.h>
using namespace std;
int main(){
    // int n;
    // cin>>n;
    // vector<int>nums;
    // while (n--){
    //     int e;
    //     cin>>e;
    //     nums.push_back(e);
    // }
    // for (int i=0;i<nums.size();i++){
    //     cout<<nums[i]*10<<endl;
    // }

    string S;
    getline(cin, S);
    cout<<S<<endl;
    vector<string>strs_;
    int start = 0;
    char res[S.size()];
    int j=0;
    for (int i = 0; i < S.size(); i++)
    {
        if (S[i] != ' ')
        {
            res[j]=S[i];
            cout<<res[j]<<endl;
            j++;
        }
    }

}