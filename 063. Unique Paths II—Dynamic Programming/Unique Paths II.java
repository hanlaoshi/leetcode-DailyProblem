class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not len(obstacleGrid) or not len(obstacleGrid[0]): return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n+1) for _ in xrange(m+1)]
        dp[0][1] = 1
        for r in xrange(1, m+1):
            for c in xrange(1, n+1):
                if obstacleGrid[r-1][c-1] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]
