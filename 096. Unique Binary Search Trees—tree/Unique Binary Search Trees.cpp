题目翻译：

给定n，有多少种结构独特的值为1...n的BST（二叉查找树）？
例如，
给定n = 3，共有5种独特的BST。

分析：
        自底向上。对于i个节点的情况，将第j个节点作为根节点，则左子树有j-1个节点，右子树有i-j个节点，左右子树不同BST种数相乘即得到j为根节点时的总数，对j从1到i求和，即得到i个节点不同BST的总数。

        另外这是一种Catalan数，公式为。 ![Tree](https://github.com/hanlaoshi/leetcode-DailyProblem/blob/master/img-storage/96.tree.png)

class Solution {
public:
    int numTrees(int n) {
        vector<int> num(n + 1, 0);
    	num[0] = 1;
    	num[1] = 1;
 
    	for(int i = 2; i <= n; i++)
    		for(int j = 1; j <= i; j++)
    		{
    			num[i] += num[j - 1] * num[i - j];
    		}
 
    	return num[n];
    }
};
