'''
因为先序中的节点为根节点,所以取出先序的第一个节点
用先序的第一个节点可以将中序分成左右子树，然后取出先序的第二个节点将左右子树再次划分
当将中序全部划分为单个点时就结束
开始递归的时候用了列表作为参数，结果内存溢出，改用下标作参数，先序和中序序列作为全局变量。

'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        return self._buildTree(0, len(preorder), 0, len(inorder))

    def _buildTree(self, pre_start, pre_end, in_start, in_end):
        if pre_start >= pre_end:
            return None
        root = TreeNode(self.preorder[pre_start])
        offset = self.inorder[in_start:in_end + 1].index(root.val)
        root.left = self._buildTree(pre_start + 1, pre_start + offset + 1, in_start, in_start + offset)
        root.right = self._buildTree(pre_start + offset + 1, pre_end, in_start + offset + 1, in_end)
        return root
