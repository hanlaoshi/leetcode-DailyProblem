Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

原题

判断一棵二叉树是否是平衡二叉树，只有当每个节点的左右两棵子树的高度差不大于1时，这棵树才是平衡的。

注意点：

无
例子:

输入:

    3
   / \
  9  20
    /  \
   15   7
  /
 14
输出: False
