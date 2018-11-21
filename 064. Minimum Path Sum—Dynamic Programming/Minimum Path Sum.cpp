#------------------多年未见出品-------------------------
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        if (n == 0) return 0;
        vector<int> d;
        d.push_back(grid[0][0]);
        int m = grid[0].size();
        for (int i = 1; i < m; i++) {
            d.push_back(d[i - 1] + grid[0][i]);
        }
        for (int i = 1; i < n; i++) {
            d[0] = d[0] + grid[i][0];
            for (int j = 1; j < m; j++) {
                d[j] = min(d[j] + grid[i][j], d[j - 1] + grid[i][j]);
            }
        }
        return d[m - 1];
    }
};
#--------------------第二种----------------------
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> minPathSum(grid);
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(i==0 || j==0)
                {//第一行或者第一列的情况
                    if(i==0) minPathSum[0][j] += minPathSum[0][j-1];
                    else minPathSum[i][0] += minPathSum[i-1][0];
                }
                else
                {//格子[i][j]的minPathSum值有两个来源:左侧格子[i][j-1],或上侧格子[i-1][j].
                 //取两者较小值，再加上当前格子的值grid[i][j] 即为结果
                    minPathSum[i][j] = min(minPathSum[i][j-1], minPathSum[i-1][j])+grid[i][j];
                }
            }
        }
        return minPathSum[m-1][n-1];
    }
};
