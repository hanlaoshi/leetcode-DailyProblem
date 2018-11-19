#--------------python(星辰出品)-----------
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

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
#-------------方法二python----------------------
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] nums = new int[m][n];
        for (int i = 0 ;i < m;i++) {
            for (int j = 0; j < n; j++) {
                if(i == 0 || j == 0)
                    nums[i][j] = 1;
                else
                    nums[i][j] = nums[i - 1][j] + nums[i][j - 1];
            }
        }
        return nums[m - 1][n - 1];
    }
}
