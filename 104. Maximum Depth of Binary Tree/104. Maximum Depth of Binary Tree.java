// 多年未见大佬出品

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
    int work(TreeNode root, int cc) {
        if (root == null) return cc;
        int tmp1 = work(root.left, cc + 1);
        int tmp2 = work(root.right, cc + 1);
        return tmp1 > tmp2 ? tmp1 : tmp2;
    }
    public int maxDepth(TreeNode root) {
        return work(root, 0);
    }
}
