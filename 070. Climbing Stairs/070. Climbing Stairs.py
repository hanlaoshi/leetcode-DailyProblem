#典型的动态规划题，递推表达式为 dp[i]=dp[i-1]+dp[i-2]，n为1时只有一种方法，n为2时有两种方法。


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        dp = [0 for __ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
