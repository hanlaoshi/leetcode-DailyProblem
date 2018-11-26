#解题思路
#一个节点的高度是它左右两棵子树的高度较大值加一，为了使代码简练，定义不平衡的子树的高度为-1，
#所以在计算每个节点的高度时，要额外判断左右两棵子树是否平衡，
#如果不平衡（左子树不平衡 | 右子树不平衡 | 左右子树高度差大于1）就直接返回-1。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isBalanced(root) >= 0

    def _isBalanced(self, root):
        if not root:
            return 0
        left, right = self._isBalanced(root.left), self._isBalanced(root.right)
        if left >= 0 and right >= 0 and abs(left - right) <= 1:
            return 1 + max(left, right)
        else:
            return -1


if __name__ == "__main__":
    None
