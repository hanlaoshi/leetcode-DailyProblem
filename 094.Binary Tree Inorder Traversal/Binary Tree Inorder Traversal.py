//--------------------------辰星出品------------------------
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        rtn = []
        if root.left: rtn.extend(self.inorderTraversal(root.left))
        rtn.append(root.val)
        if root.right: rtn.extend(self.inorderTraversal(root.right))
        return rtn

【思路】

二叉树遍历：

前序遍历：根结点、左子树、右子树

中序遍历：左子树、根结点、右子树

后序遍历：左子树、右子树、根结点

如下一棵二叉树，利用栈其整个过程为：

![stack](https://github.com/hanlaoshi/leetcode-One-topic-per-day/blob/master/img-storage/94.stack.png?raw=true)

l  根结点G入栈，若入栈的结点存在左子树，则依次入栈G/D/A，直至A发现其左子树为空，停止入栈，此时栈stack = [G,D,A]。

l  A出栈，并对A进行遍历，发现A没有右子树，根据中序遍历，需要遍历A的根节点D，D出栈，D存在右孩子，将其右孩子F入栈，F有左子树E，E入栈，此时stack = [G,F,E]，res=[A,D]

l  E出栈，并对E进行遍历，发现没有右子树，根据中序遍历，需要遍历E的根结点F，F出栈，此时栈为stack = [G],res = [A,D, E, F]

l  G出栈，并遍历G，G有右子树，将右子树M入栈，此时栈为stack = [M],res = [A,D, E, F,G]

l  右子树根结点M，按照中序遍历规则重复以上步骤：

         M存在左子树H入栈，stack = [M,H],res= [A,D, E, F,G]

         H出栈，遍历H，发现H没有右子树，根据中序遍历，需要遍历H的根结点M，M有右子树Z，Z入栈，此时stack = [Z],res = [A,D, E, F,G,H,M]

         Z出栈，遍历Z，发现Z没有右子树，此时stack= [],res = [A,D, E, F,G,H,M,Z]

//【Python实现】

//方法一：非递归方式


#输出二叉树的中序遍历，非递归方式
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.iterative_inorder(root, res)
        print(res)
        return res
    def iterative_inorder(self, root, res):#迭代中序遍历
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
 
if __name__ == '__main__':
    S = Solution()
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(6)
    l7 = TreeNode(7)
    root = l1
    l1.left = l2
    l1.right = l3
    l2.left = l4
    l2.right = l5
    l3.left = l6
    l3.right = l7
    S.inorderTraversal(root)                

//方法二：递归方式
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self. recursive_inorder (root, res)
        print(res)
        return res
    def recursive_inorder(self, root, res):#递归中序遍历
        if root:
            self.recursive_inorder(root.left, res)
            res.append(root.val)
            self.recursive_inorder(root.right, res)
            
            
if __name__ == '__main__':
    S = Solution()
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(6)
    l7 = TreeNode(7)
    root = l1
    l1.left = l2
    l1.right = l3
    l2.left = l4
    l2.right = l5
    l3.left = l6
    l3.right = l7
    S.inorderTraversal(root)
