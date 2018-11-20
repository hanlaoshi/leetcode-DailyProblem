class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(); //行数
        int n = obstacleGrid[0].size();//列数
        int p[m][n];
       
       //第一列赋值 
        int k = 0;
        while(k < m && obstacleGrid[k][0] != 1)
            p[k++][0] = 1;
       //如果遇到了障碍物则它及其后面的值都为0
        while(k < m)
            p[k++][0] = 0;
        
        //第一行赋值
        k = 0;
        while(k < n && obstacleGrid[0][k] != 1)
            p[0][k++] = 1;
        while(k < n)
            p[0][k++] = 0;
        
        for(int i = 1; i < m; i++)
            for(int j = 1; j < n; j++){
                if(obstacleGrid[i][j] == 1) //如果遇到障碍物，则该位置的值为0
                    p[i][j] = 0;
                else
                    p[i][j] = p[i - 1][j] + p[i][j - 1];
            }
        return p[m-1][n-1];
    }
};
