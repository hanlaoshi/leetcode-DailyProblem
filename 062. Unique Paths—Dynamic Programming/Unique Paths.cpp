class Solution {
public:
    int dp[105][105];
    int uniquePaths(int m, int n) {
        for(int i=0;i<n;++i)
            for(int j=0;j<m;++j)
                dp[i][j]=i*j==0?1:(dp[i-1][j]+dp[i][j-1]);
         return dp[n-1][m-1];
    }
};
