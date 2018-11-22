题目翻译：

给定n，有多少种结构独特的值为1...n的BST（二叉查找树）？
例如，
给定n = 3，共有5种独特的BST。

分析：
        自底向上。对于i个节点的情况，将第j个节点作为根节点，则左子树有j-1个节点，右子树有i-j个节点，左右子树不同BST种数相乘即得到j为根节点时的总数，对j从1到i求和，即得到i个节点不同BST的总数。

        另外这是一种Catalan数，公式为。 ![Tree](https://github.com/hanlaoshi/leetcode-DailyProblem/blob/master/img-storage/96.tree.png)


class Solution:
    # @return an integer
    def numTrees(self, n):
        num = [0 for i in range(n + 1)]
        num[0] = 1
        num[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                num[i] += num[j - 1] * num[i - j]
        
        return num[n]
