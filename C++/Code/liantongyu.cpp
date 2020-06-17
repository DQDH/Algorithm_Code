#include <iostream>
#include <vector>
#include <queue>

using namespace  std;

struct Point
{
    int r;
    int c;
    Point(int r_, int c_) : r(r_), c(c_){}
    Point(const Point& p) : r(p.r), c(p.c){}
};

class Solution
{
public:
    int m;
    int n;
    //判断索引点不要越界，该点之前没有访问过，该点是有效的点
    bool isvalid(int i, int j, vector<vector<int>>& matrix, vector<vector<bool>>& mask)
    {
        return i>=0 && i<m && j>=0 && j<n && !mask[i][j] && matrix[i][j]==1;
    }
   //将合适的点加入到队列中，并标记其被访问过
    void add(int i, int j, vector<vector<int>>& matrix, queue<Point>& q, vector<vector<bool>>& mask)
    {
        if(isvalid(i, j, matrix, mask))
        {
            q.push(Point(i,j));
            mask[i][j]=true;
        }
    }
    //主代码，两重for循环+一个queue
    vector<vector<Point>> bwlabel(vector<vector<int>> &matrix)
    {
        m=matrix.size(); 
        n=matrix[0].size();
        vector<vector<Point>> res;
        vector<Point> tmp;
        vector<vector<bool>> mask(m, vector<bool>(n,false));
        for(int i=0; i<m;i++)
        {
            for(int j=0; j<n; j++)
            {
                if(mask[i][j] || matrix[i][j] == 0)
                    continue;
                tmp.clear();
                queue<Point> q;
                q.push(Point(i,j));
                mask[i][j] = true;
                while(!q.empty())
                {
                    Point t = q.front();
                    q.pop();
                    tmp.push_back(t);
                    //根据四邻域定义得来
                    add(t.r-1, t.c, matrix, q, mask);
                    add(t.r+1, t.c, matrix, q, mask);
                    add(t.r, t.c-1, matrix, q, mask);
                    add(t.r, t.c+1, matrix, q, mask);
                }
                res.push_back(tmp);
            }
        }
        return res;
    }
};
int main()
{
    vector<vector<int>> m = {
        {1,1,0,0,0},
        {1,0,1,0,0},
        {0,1,1,0,0},
        {0,0,0,1,0},
        {0,0,0,0,1},
        {0,0,0,0,0}
    };
    vector<vector<int>> n = {{}};
    Solution s;
    vector<vector<Point>> res = s.bwlabel(m);
    vector<vector<Point>> rss = s.bwlabel(n);
    return 0;
}
