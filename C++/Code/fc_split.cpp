#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>

using namespace std;

int supersplit(const string& s, vector<string>& v, const char& c)  //const string& c
{
	string::size_type pos1, pos2;
	size_t len = s.length();
	pos2 = s.find(c);
	pos1 = 0;
	while (string::npos != pos2)
	{
		v.emplace_back(s.substr(pos1, pos2 - pos1));

		pos1 = pos2 + 1;//pos2 + c.size()
		pos2 = s.find(c, pos1);

	}
	if (pos1 != len) v.emplace_back(s.substr(pos1));
	
	return 0;
}
int main(int argc, char *argv[])
{
	string s;
	vector<string> v;
	//vector<string> vi;  
	char c = ',';
	getline(cin, s);
	supersplit(s, v, c);
	

	for (int i = 0; i < v.size(); i++) 
	{
		cout << v[i] << c;
	}
	system("pause");
	return 0;
}