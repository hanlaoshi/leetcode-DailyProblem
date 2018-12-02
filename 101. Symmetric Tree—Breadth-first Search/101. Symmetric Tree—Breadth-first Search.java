//1. 树是空的，true。

//2. 判断这棵树的左子树和右子树是否对称。

//3. 两棵子树的对称条件：根节点相等，左子树的左子树和右子树的右子树对称，左子树的右子树和右子树的左子树对称：

 

//       2            2
//      / \          / \
//     3   4        4   3
//    / \ / \      / \ / \
//   5  6 7  8    8  7 6  5
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        else {
            return isSymmetric(root.left, root.right);
        }
    }
    private boolean isSymmetric(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }
        else if (left == null || right == null) {
            return false;
        }
        return left.val == right.val && isSymmetric(left.left, right.right) && isSymmetric(left.right, right.left);
    }
}
