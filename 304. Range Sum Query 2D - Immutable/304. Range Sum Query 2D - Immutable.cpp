#-----------------------（好名字）贡献-----------------------------
class NumMatrix {
public:
    NumMatrix(vector<vector<int>> matrix) {
        if(matrix.size() && matrix[0].size() && matrix[0][0]){
            int sum =0;
        vector<int> row(matrix[0].size()+1,0);
        this->matrix.push_back(row);
        for(int i=0;i<matrix.size();i++){
            sum=0;
            row.clear();
            row.push_back(0);
            for(int j=0;j<matrix[0].size();j++){
                sum += matrix[i][j];
                if(i==0)
                    row.push_back(sum);
                else
                    row.push_back(sum + this->matrix[i][j+1]);
            }
            for(int m=0;m<matrix[0].size()+1;m++)
                cout<<" "<<row[m];
            this->matrix.push_back(row);
        }
        }
        
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return  matrix[row2+1][col2+1] - matrix[row2+1][col1] - matrix[row1][col2+1] + matrix[row1][col1];
    }
    private:
    vector<vector<int > > matrix;
};
#------------------------第二种方法---------------------------------
class NumMatrix {
public:
    NumMatrix(vector<vector<int>> matrix) {
       int m=matrix.size();
       if(!m) return;
       int n=matrix[0].size();
       sums.resize(m);
       for(int i=0;i<m;i++) sums[i].resize(n);
        if(!n) return;
        sums[0][0]=matrix[0][0];
        //以下是初始化
       for(int i=1;i<m;i++)
       {
          sums[i][0]=sums[i-1][0]+matrix[i][0];
       }
       for(int i=1;i<n;i++)
       {
           sums[0][i]=sums[0][i-1]+matrix[0][i];
       }
       for(int i=1;i<m;i++)
       {
           for(int j=1;j<n;j++)
           sums[i][j]=sums[i][j-1]+sums[i-1][j]-sums[i-1][j-1]+matrix[i][j];
       }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
       if(row1==0&&col1==0)
       return sums[row2][col2];
       else if(row1==0)
       return sums[row2][col2]-sums[row2][col1-1];
       else if(col1==0)
       return sums[row2][col2]-sums[row1-1][col2];
       else return sums[row2][col2]-sums[row2][col1-1]-sums[row1-1][col2]+sums[row1-1][col1-1];
    }
    private:
    vector<vector<int>> sums;
};
 
/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
