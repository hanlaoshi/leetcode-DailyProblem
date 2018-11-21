#-------------第一种---------------
class Solution {
    public int minPathSum(int[][] grid) {
        if(grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0){
            return 0;
        }
        int row = grid.length;
        int col = grid[0].length;
        int[][] dp = new int[row][col];
        dp[0][0] = grid[0][0];
        for (int i = 1; i < row; i++) {
			dp[i][0] = dp[i - 1][0] + grid[i][0];
		}
		for (int j = 1; j < col; j++) {
			dp[0][j] = dp[0][j - 1] + grid[0][j];
		}
		for (int i = 1; i < row; i++) {
			for (int j = 1; j < col; j++) {
				dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
			}
		}
		return dp[row - 1][col - 1];
    }
}
#-------------第二种leetcode最快的---------------
class Solution {
        private int[][] grid;
        private int sum;
        private int[][] temp;
        public int minPathSum(int[][] grid) {
            this.grid=grid;
            temp=new int[grid.length][grid[0].length] ;
            int x=0;
            int y=0;



            return minPath(0,0);
        }
        private int minPath(int x,int  y){
            if(x==grid.length-1&&y==grid[0].length-1){
                return grid[x][y];
            }
            if(x>grid.length-1||y>grid[0].length-1){
                return Integer.MAX_VALUE;
            }
            if(temp[x][y]!=0){
                return temp[x][y];
            }
            temp[x][y]=grid[x][y]+Math.min(minPath(x+1,y),minPath(x,y+1));
            return temp[x][y];
        }
}
