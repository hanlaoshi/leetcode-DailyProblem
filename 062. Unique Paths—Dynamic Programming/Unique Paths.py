#--------------python(星辰出品)-----------
class Solution:
    def recursion_paths(x, y):
            n = 0
            if x:
                n += recursion_paths(x - 1, y)

            if y:
                n += recursion_paths(x, y - 1)              
            if x == 0 and y == 0:
                n = 1
            return n

        return recursion_paths(m - 1, n - 1)

#--------------python第二种-----------
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0
        dp = [[0]*n]*m
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
