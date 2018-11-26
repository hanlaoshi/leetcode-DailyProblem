Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

`Example 1:`

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

`Output: true`

`Example 2:`

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

`Output: false`

`Example 3:`

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

`Output: false`

`原题`

判断两棵二叉树是否相等。两棵二叉树仅在它们的形状相同且每个节点的值相等时才判为相等。

`注意点：`

无

`例子：`

`输入:`

      2           2
p =  / \    q =  / \
    1   3       1   3
    
`输出: True`
