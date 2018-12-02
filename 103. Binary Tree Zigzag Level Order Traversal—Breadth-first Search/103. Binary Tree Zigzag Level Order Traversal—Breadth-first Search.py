#思路：和上一篇文章102的思路基本相同，只是在res中加入templist时加了一步判断flag是否为负的步骤，
#如果为负，表示是偶数次遍历应该从右往左，将templist更新为逆序

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        flag = 1
        while queue:
            templist = []
            length = len(queue)
            for i in range(length):
                temp = queue.pop(0)
                templist.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            if flag == -1:
                templist=templist[::-1]
            res.append(templist)
            flag *= -1
        return res
