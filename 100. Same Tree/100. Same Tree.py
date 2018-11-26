#解题思路
#树相关的问题一般用递归的方法最好理解。如果两棵树对应的节点都为空，则相等；
#如果值相等，那么就分别判断它们的左右子树是否相等，否则认为两棵树不相等。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    None
