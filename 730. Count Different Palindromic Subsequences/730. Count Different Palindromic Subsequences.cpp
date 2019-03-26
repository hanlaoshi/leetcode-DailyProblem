class Solution 
{
public:
    int countPalindromicSubsequences(string s) 
    {
        const int M = 1e9+7;
        int n = s.length();
        vector<vector<int>> dp(n,vector<int>(n,0));
        for (int i = 0; i < n; i++)
            dp[i][i] = 1;

        for (int len = 1; len <= n; len++)
        {
            for (int i = 0; i + len < n; i++)
            {
                int j = i + len;
                if (s[i] == s[j])
                {
                    int left = i + 1, right = j - 1;
                    while (left <= right && s[left] != s[i])
                        left++;
                    while (left <= right && s[right] != s[i])
                        right--;
                    if (left > right)
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2;
                    else if (left == right)
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1;
                    else
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1];
                }
                else
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1];

                dp[i][j] = (dp[i][j] < 0) ? dp[i][j] + M : dp[i][j] % M;
            }
        }
        return dp[0][n - 1];
    }
};
