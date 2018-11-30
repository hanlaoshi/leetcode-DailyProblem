#解题思路
#直接通过递归来解决，判断一个节点时，先把要求的值先减去该节点的值，如果剩下要求的值为0且当前的节点就是一个叶子节点，
#那么从根节点到当前节点的路径就符合题目的要求。否则就要继续递归当前节点的左右节点。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        sum -= root.val
        if sum == 0 and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


if __name__ == "__main__":
    None

    # 方法2   辰星大佬 出品
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        path_sum, dp, cnt = [[root.val]], [[root]], 0
        while True:
            nxt = cnt + 1
            dp.append([])
            path_sum.append([])
            for i, node in enumerate(dp[cnt]):
                if path_sum[cnt][i] == sum and not node.left and not node.right:
                    return True
                if node.left:
                    path_sum[nxt].append(path_sum[cnt][i] + node.left.val)
                    dp[nxt].append(node.left)
                if node.right:
                    path_sum[nxt].append(path_sum[cnt][i] + node.right.val)
                    dp[nxt].append(node.right)
            if dp[nxt] == []:
                break
            cnt = nxt
        return False
    
  


#  方法3   多年文件大佬 出品
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False;
        if root.left: 
            if self.hasPathSum(root.left, sum - root.val): return True
        if root.right: 
            if self.hasPathSum(root.right, sum - root.val): return True
        if (not root.left) and (not root.right) and sum == root.val: return True
        return False
