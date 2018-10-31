//方法3（c++版本）动态规划实现
bool isMatch(string s, string p) {
       int lens = s.length(), lenp = p.length();
 bool ** dp = new bool*[lens + 2];
 for (int i = 0; i < lens+2; i++)
  dp[i] = new bool[lenp + 2];
 
 for (int i = 0; i < lens+2; i++)
  for (int j = 0; j < lenp+2; j++)
   dp[i][j] = false;
 dp[0][0] = true;
 
 for (int i = 1; i < lenp; i++)
  if (p[i] == '*'&&dp[0][i - 1])
   dp[0][i + 1] = true;
 
 for (int i = 0; i < lens; i++)
  for (int j = 0; j < lenp; j++)
  {
   if (s[i] == p[j] || p[j] == '.')
    dp[i + 1][j + 1] = dp[i][j];
   else if (p[j] == '*')
   {
    if (p[j - 1] != s[i] && p[j - 1] != '.')
     dp[i + 1][j + 1] = dp[i + 1][j - 1];
    else
     dp[i + 1][j + 1] = (dp[i + 1][j] || dp[i][j + 1] || dp[i + 1][j - 1]);
   }
  }
 
 
 return dp[lens][lenp];
    }
