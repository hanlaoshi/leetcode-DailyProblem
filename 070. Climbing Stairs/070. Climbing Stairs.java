/*

这道题就是经典的讲解最简单的DP问题的问题。。

假设梯子有n层，那么如何爬到第n层呢，因为每次只能怕1或2步，那么爬到第n层的方法要么是从第n-1层一步上来的，要不就是从n-2层2步上来的，所以递推公式非常容易的就得出了：

dp[n] = dp[n-1] + dp[n-2]

如果梯子有1层或者2层，dp[1] = 1, dp[2] = 2，如果梯子有0层，自然dp[0] = 0 
*/
public int climbStairs(int n) {
        if(n==0||n==1||n==2)
            return n;
        int [] dp = new int[n+1];
        dp[0]=0;
        dp[1]=1;
        dp[2]=2;
        
        for(int i = 3; i<n+1;i++){
            dp[i] = dp[i-1]+dp[i-2];
        }
        return dp[n];
    }
