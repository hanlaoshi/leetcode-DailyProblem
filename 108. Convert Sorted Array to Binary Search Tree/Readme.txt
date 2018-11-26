Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 
 原题
 
给定一个升序的序列，将它转化为高度平衡的二叉搜索树。
注意点：

同一个序列转化成的二叉搜索树可能有多种
例子:

输入: nums = [1,2,3]
输出:

  2
 / \
1   3
