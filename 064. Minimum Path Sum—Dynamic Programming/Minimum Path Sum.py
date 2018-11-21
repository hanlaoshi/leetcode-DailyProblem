#----------------辰星出品-------------------------
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0
        min_grid = [[None]*m for i in range(n)]
        min_grid[0][0] = grid[0][0]
        for i in range(1, m):
            min_grid[0][i] = min_grid[0][i - 1] + grid[0][i]
        for i in range(1, n):
            min_grid[i][0] = min_grid[i - 1][0] + grid[i][0]
        for i in range(1, n):
            for j in range(1, m):
                min_grid[i][j] = min(min_grid[i - 1][j],min_grid[i][j - 1]) + grid[i][j]
        return min_grid[n - 1][m - 1]
#-----------------python快速法--------------------
class Solution:
    def minPathSum(self, grid):
        n=len(grid[0])
        m=len(grid)
        dp = [[0]*n for i in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[i][0]=grid[i][0]+dp[i-1][0]
        for j in range(1,n):
            dp[0][j]=grid[0][j]+dp[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i][j-1],dp[i-1][j])+grid[i][j];
        return dp[m-1][n-1]              
        
        
