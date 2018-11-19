A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


![Roman_to_int](https://github.com/hanlaoshi/leetcode-DailyProblem/blob/master/img-storage/Unique_Paths.png)

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

思路：

第一反应是递归，如何递归？比如每个格子能够走到终点的路径数 = 从当前格子右边的格子开始的路径数 + 从当前格子下边的格子开始的路径数。所以可以以此为条件进行递归，然后递归的终止条件是，某一行或者某一列只有一格，这种时候其路径数只有一条，这个时候跳出就行了。

但是！！！这样做的一个问题是，势必有的格子会重复计算，比如说原题目中，小机器人所在格的右下格，这个格子在递归中，被计算了两次（分别是其上面的格子和左边的格子）。

回想一下用递归的方式计算斐波拉契数列，其时间复杂度是O(2^N)，当N越来越大的时候，消耗的时间会指数增大。因此递归实现这个问题也是同理，用递归实现了一下，果不其然，结果显示超时。

那么什么样的方式比较好？想一下斐波拉契数的解决方式：从0和1开始，逐步往上走。其实这个问题也可以看作是一个逐步往上走的过程。因为每一个格子的路径数上面也已经交代了， 之前的思路是要求哪个格子，就从这个格子出发往下层计算。现在颠倒一下，先求好下层的路径数，需要求哪个格子的路径数，根据上述计算公式直接加起来即可。

因此我们构建一个二维数组来存储每个格子的路径数，从终点处开始向上推。如果碰到某行或者某列是1的情况，那么路径数就直接为1，否则，该格子的路径数等于其下面的格子路径数加上其右边的格子的路径数。
