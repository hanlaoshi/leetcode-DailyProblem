Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

原题

判断一棵二叉树是否有一条从根节点到某一叶子节点的路径，该路径上所有节点的和为一个特定值。
注意点：

无
例子:

输入: sum = 12
    3
   / \
  9  20
    /  \
   15   7
  /
 14
输出: True (3->9)
