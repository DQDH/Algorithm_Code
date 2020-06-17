#include<stdio.h>
#include<iostream>
#include<cstring>

using namespace std;
const int N = 1000005;
int k[N];
void fa(){
 memset(k, 0, sizeof(k));
 k[0] = k[1] = 0;
 for (int i = 2; i<N; i++){
  if (i % 2 == 0){
   k[i] = i / 4 * 2 + k[i - 2];
  }
  else{
   k[i] = (i + 1) / 4 + k[i - 1] - 1;
  }
 }
}
int main(){
 int n; 
 cin >> n;
 fa();
 while (n--){
  int x;
  cin >> x;
  for (int i = 0; i<N; i++){
   if (k[i] >= x){
    cout << i << endl;
    break;
   }
  }
 }
 return 0;
}