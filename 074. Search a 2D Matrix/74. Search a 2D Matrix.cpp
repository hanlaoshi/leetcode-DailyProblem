/*
递归实现。

        如果节点为空则返回false；

        如果左右子节点均为空，则返回节点值是否等于sum；

        否则递归判断其左右子树，新sum为sum减去节点的值。


*/
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode *root, int sum) {
        if(root == NULL)
    	{
    		return false;
    	}
 
    	if(root->left == NULL && root->right == NULL)
    	{
    		return sum == root->val;
    	}
 
    	return hasPathSum(root->left, sum - root->val) 
    	    || hasPathSum(root->right, sum - root->val);
    }
};

