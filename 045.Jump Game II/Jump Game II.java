/*
参考了http://blog.csdn.net/linhuanmars/article/details/21356187，
这道题和Jump Game都是利用动态规划的思想。区别是，上一道题维护的全局最优是maxcover，一旦maxcover大于总长度，那么说明能跳到结尾。

而这道题除了维护maxcover外，还需要考虑维护最小步数，最小步数的维护靠maxcover作为每一步能跳的长度
*/

public int jump(int[] A) {
        if(A==null||A.length==0)
            return 0;
        
        int maxcover = 0;
        int step = 0;
        int lastcover = 0;
        for(int i = 0; i<=maxcover&&i<A.length;i++){
            if(i>lastcover){
                step++;
                lastcover = maxcover;
            }
            
            if(A[i]+i>maxcover)
                maxcover = A[i]+i;
        }
        
        if(maxcover<A.length-1)
            return 0;
        return step;
    }
