
// 多年未见大佬出品

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
    int work(TreeNode* root, int cc) {
        if (root == NULL) return cc;
        return max(work(root->left, cc + 1), work(root->right, cc + 1));
    }
public:
    int maxDepth(TreeNode* root) {
        return work(root, 0);
    }
};
