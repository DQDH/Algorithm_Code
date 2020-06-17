class solution(object):
    def get_max(self,nums):
        num=0
        if len(nums)<2:
            return nums[0],0
        if nums[0] < nums[-1]:
            num += nums[-1]
            return num,1
        else:
            nums += nums[0]
            return num,0
    def Q2(self,nums):
        m,n=0,len(nums)-1
        xm=0
        dm=0
        while m<n:
            num,x=self.get_max(nums[m:n+1])
            xm+=num
            if x:
                n-=1
            else:
                m+=1
            num, x = self.get_max(nums[m:n+1])
            if x:
                n -= 1
            else:
                m += 1
            dm+=num
        return 'No' if dm>xm else 'Yes'
nums=list(map(int,input().split()))
print(solution().Q2(nums))

'''
#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include "algorithm"
#include<sstream>
using namespace std;

int main()
{
    string line;
    getline(cin, line);
    stringstream s(line);
    vector<int> nums;
    int x;
    while (s >> x)
        nums.push_back(x);
    int length=nums.size();
    if(length < 3)
        return true;  
    vector<vector<int>> dfs(length,vector<int>(length,0));  
    int res=0;
    for(int i=0;i<length;++i)
    {
        res+=nums[i];    
        dfs[i][i]=nums[i];    
    }
    for(int l=1;l<length;++l)  
    {
        for(int i=0;i<length-l;++i)
        {
            int j=i+l;
            if(l==1)
                dfs[i][j]=max(nums[i],nums[j]); 
            else
                dfs[i][j]=max(nums[i]+min(dfs[i+1][j-1],dfs[i+2][j]),nums[j]+min(dfs[i][j-2],dfs[i+1][j-1]));
        }

    }
    if(dfs[0][length-1] >= res-dfs[0][length-1])
    {
        cout<<"Yes"<<endl;
    }
    else
    {
        cout<<"No"<<endl;
    }
    return 0;
}
'''