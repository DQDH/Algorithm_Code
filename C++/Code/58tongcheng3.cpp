#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int n;
    while (cin >> n)
    {
        vector<int> v(n, 0);
        for (int i = 0; i < n; ++i)
            cin >> v[i];
        if (n == 0 || n == 1)
        {
            cout << n << endl;
            continue;
        }
        vector<int> dp1( n, 0 ); 
        vector<int> dp2( n, 0 ); 
        dp1[n - 1] = 1;
        for (int i = n - 2; i >= 0; --i){
            if (v[i] < v[i + 1])
                dp1[i] = dp1[i + 1] + 1;
            else
                dp1[i] = 1;
        }
        dp2[0] = 1;
        for (int i = 1; i < n - 1; ++i){
            if (v[i] > v[i - 1])
                dp2[i] = dp2[i - 1] + 1;
            else
                dp2[i] = 1;
        }
        int res = 1;
        int m = 1;
        for (int i = 0; i < n - 1; ++i)
        {
            if (i == 0)
                m = dp1[i + 1] + 1;
            else if (i == n - 1)
                m = dp2[i - 1] + 1;
            else if (v[i - 1] + 1 < v[i + 1])
                m = dp1[i + 1] + dp2[i - 1] + 1;
            else
                m = max(dp1[i + 1], dp2[i - 1]) + 1;
            if (m > res)
                res = m;
        }

        cout << res << endl;
    }
}