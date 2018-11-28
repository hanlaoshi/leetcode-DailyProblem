/*
目的是要得到一个平衡二叉树，也就说是每棵数的根节点应该是整棵树上结点的中位数。
所以取数组的中位数作为根节点，中位数左边为左子树的数组，右边为右子数的数组。以此类推。
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        TreeNode* root;
        root = helper(root, nums, 0, nums.size() - 1);
        return root;
    }

    TreeNode* helper(TreeNode* root, vector<int>& nums, int start, int end) {
        if (start > end) {
            return NULL;
        }
        root = new TreeNode(0);
        root->val = nums[(start + end + 1) / 2];
        root->left = helper(root->left, nums, start, (start + end + 1) / 2 - 1);
        root->right = helper(root->right, nums, (start + end + 1) / 2 + 1, end);
        return root;
    }
};
