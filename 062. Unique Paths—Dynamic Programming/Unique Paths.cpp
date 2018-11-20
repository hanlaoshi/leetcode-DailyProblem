class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> info(n,vector<int>(m,0));
        for(int i=0;i<m;++i)
        {
            info[0][i]=1;
        }
        for(int i=0;i<n;++i)
        {
            info[i][0]=1;
        }
        for(int i=1;i<m;++i)
        {
            for(int j=1;j<n;++j)
            {
                info[j][i]=info[j-1][i]+info[j][i-1];
            }
        }
        return info[n-1][m-1];
    }
};
