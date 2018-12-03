#--------------多年未见cpp写的深搜---------------------
class Solution {
    bool sameTree(TreeNode* a, TreeNode* b) {
        if (a == NULL && b == NULL) return true;
        if (a == NULL || b == NULL) return false;
        if (a->val != b->val) return false;
        return sameTree(a->left, b->right) && sameTree(a->right, b->left);
    }
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;
        return sameTree(root->left, root->right);
    }
};
#----------------------二---------------------
#说明: 
#如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

#思路：
#递归终止条件：：两棵树同时遍历到空（true），仅一棵树遍历到空（false），两棵树遍历到的节点值不同（false）。
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
private:
    bool rec(TreeNode* leftR,TreeNode* rightR){
        if(leftR == NULL && rightR == NULL)
            return true;
        if(leftR == NULL || rightR == NULL)
            return false;
        if(leftR->val != rightR->val)
            return false;
        return (rec(leftR->left,rightR->right) && rec(leftR->right,rightR->left));
    }
public:
    bool isSymmetric(TreeNode* root) {
        if(root == NULL)
            return true;
        return rec(root->left,root->right);      
    }
};
