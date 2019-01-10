class Solution {
    public int maximalRectangle(char[][] matrix) {
        if(matrix.length==0){
            return 0;
        }
        
        int res=0;
        int[][] nums=new int[matrix.length][matrix[0].length];
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if(matrix[i][j]=='1'){
                    nums[i][j]=1;
                }else{
                    nums[i][j]=0; 
                }
            }
        }
        
        //只含0，1的数组转换成不只是包含0，1的统计形式
        for(int i=0;i<matrix[0].length;i++){
            int sum1=1;
            for(int j=matrix.length-1;j>=0;j--){
                if(nums[j][i]==1){
                    nums[j][i]=sum1;
                    sum1++;
                }else{
                    sum1=1;
                }
            }
        }
        
        
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if(nums[i][j]!=0){
                    //连续非0数的个数
                    int sum2=1;
                    //连续非0数中最小值
                    int min=nums[i][j];
                    
                    if(nums[i][j]>res){
                        res=nums[i][j];
                    }
                    for(int k=j+1;k<matrix[0].length;k++){
                        if(nums[i][k]!=0){
                            sum2++;
                            if(nums[i][k]<min){
                                min=nums[i][k];
                            }
                            int tem_res=sum2*min;
                            if(tem_res>res){
                               res=tem_res;
                            }  
                        }else{
                            break;
                        }
                    }
                                        
                }
            }
        }
        
        return res;
    }
}
