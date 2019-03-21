class NumMatrix {
 
    int[][] sum;
    int m;
    int n;
    
    public NumMatrix(int[][] matrix) {
        if(matrix == null) return;
        this.m = matrix.length;
        if(m==0) return;
        this.n = matrix[0].length;
        if(n == 0) return ;
        sum = new int[m][n];
        for(int i = 0 ; i < m  ; i++){
            for(int j = 0; j < n ; j++){
                if(i > 0) sum[i][j] += sum[i-1][j];
                if(j > 0) sum[i][j] += sum[i][j-1];
                sum[i][j] += matrix[i][j];
                if(i > 0 && j > 0) sum[i][j] -= sum[i-1][j-1];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        if(sum == null) return 0;
        if(row1 > m || row2 > m || col1 > n || col2 > n) return 0;
        int ans = sum[row2][col2];
        if(row1>0) ans -= sum[row1-1][col2];
        if(col1>0) ans -= sum[row2][col1-1];
        if(row1 > 0 && col1 >0) ans += sum[row1-1][col1-1];
        return ans;
    }
}
 
/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
