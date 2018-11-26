/*
分析：
        1 如果两个节点都为空，则相等。

        2 如果仅有一个节点为空，则不等。

        3 如果节点的值相等，并且左子树和右子树分别相等，则返回相等，否则返回不等。
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
    bool isSameTree(TreeNode *p, TreeNode *q) {
    	if(!p && !q)
    	{
    		return true;
    	}
 
    	if(!p || !q)
    	{
    		return false;
    	}
 
    	return p->val == q->val && isSameTree(p->left, q->left)
    							&& isSameTree(p->right, q->right);
    }
};


//第二种方法   by 多年未见 大佬出品

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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == NULL && q == NULL) return true;
        if (p == NULL) return false;
        if (q == NULL) return false;
        if (p->val != q->val) return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
