#include <iostream>
#include <queue>
#include <vector>
#include <sstream>

using namespace std;

struct Node {
	int val;
	Node* left;
	Node* right;
    Node(int val_):val(val_), left(NULL), right(NULL) {}
};

bool isNum (string str) {
	stringstream sin(str);
	int d;
	char c;
	if (!(sin >> d))
	  return false;
	if (sin >> c)
	  return false;

	return true;
}

int s2int ( const string& s) {
    stringstream ss;
	ss<<s;
	int ret;
	ss>>ret;
	return ret;
}

vector<string> split(const string& s, const string& delmiter) {
	vector<string> result;
	typedef string::size_type string_size;
    string_size i = 0;
     
    while(i != s.size()){
        int flag = 0;
        while(i != s.size() && flag == 0){
            flag = 1;
            for(string_size x = 0; x < delmiter.size(); ++x) {
                if(s[i] == delmiter[x]){
                	++i;
                    flag = 0;
                    break;
                }
            }
        }
         
        flag = 0;
        string_size j = i;
        while(j != s.size() && flag == 0){
            for (string_size x = 0; x < delmiter.size(); ++x) {
			    if(s[j] == delmiter[x]){
                    flag = 1;
                    break;
                }
			}
            if(flag == 0)
				++j;
        }//end while
        if(i != j){
            result.push_back(s.substr(i, j-i));
            i = j;
        }
    }
    return result;
}

Node* createBTree (vector<string>& v, int index) {
	Node* node = NULL;

	if (index < v.size()) {
		if (isNum(v[index]) == false) {
			return NULL;
		}
		node = new Node(s2int(v[index]));
		node->left = createBTree(v, index * 2 + 1);
		node->right = createBTree(v, index * 2 + 2);
		return node;
	}
	return node;
}

int levelOrder(Node* root) {
	vector<double> res;
    queue<Node*> q;
        q.push(root);

        while(!q.empty()){

            double sum = 0, count = 0;

            queue<Node*> temp;

            while(!q.empty()){

                Node* n = q.front();

                q.pop();

                sum += n->val;
 
               count++;
 
               if(n->left!=NULL){

                    temp.push(n->left);

                }

                if(n->right!=NULL){
 
                   temp.push(n->right);

                }

            }

            q = temp;
			res.push_back((sum*1.0/count));
			cout<<sum*1.0/count;

        }
	int r;
	float rr=0.0;
	for (int i;i<res.size();i++){
		if (res[i]>=rr){
			r=i;
		}
	}

        return r;

}

int main() {
    string inString;
	int len = 0;
    cin>>inString;
	//vector<string> res = split(inString, " ");
	vector<string> res;
    if (isNum(inString)) {
		len = s2int(inString);
	}
	for (int i = 0; i < len; i++) {
		cin>>inString;
		res.push_back(inString);
	}
	/*
	for (int i = 0; i < res.size(); i++) {
	    cout<<res[i]<<"	";
	}
	cout<<endl;
	*/
    Node* root = createBTree(res,0);

    int ret = levelOrder(root);
    cout<<ret<<endl;
    return 0;
}