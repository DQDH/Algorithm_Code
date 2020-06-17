#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int com(string &pa, string &sub)
{
 int first = pa.find(sub[0]);
 if (first == -1)
  return 0;
 else
 {
  if (sub.length() == 1)
   return 1;
  else
  {
   for (int i = 1; i < sub.length(); i++)
   {
    first = pa.substr(first, pa.length() - 1).find(sub[i]);
    if (first == -1)
     return 0;
   }
  }
 }
 if (first!= -1)
 {
     return 1;
 }
 return 0;
}

int main()
{
 int row;
 cin >> row;
 vector<int> result(row);
 string ss;
 for (int i = 0; i < row; i++)
 {
  string str1,str2;
  cin >> str1;
  cin >> str2;
  result[i]=com(str1, str2);
 }
 for (int i = 0; i < row; i++)
 {
  if (result[i])
   ss = "SUB";
  else
   ss = "NO";
  cout << ss << endl;
 }
 return 0;
}