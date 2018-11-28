/*
本题解题思路还是从递归出发，但是要结合二叉查找树的定义，每次将数组二分中间值作为根节点，
依次递归二分并将中间值赋值给根节点，最后返回根结点，递归返回的临界条件是：左索引大于右索引
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
        if(nums.size()==0)
            return NULL;
        return sortedSub(nums,0,nums.size()-1);
        
    }
private: 
    TreeNode* sortedSub(vector<int>& nums, int l, int r)  {  
    if(l>r)  
        return NULL;  
    int m = (l+r)/2;  
    TreeNode* root = new TreeNode(nums[m]);  
    root->left = sortedSub(nums,l,m-1);  
    root->right = sortedSub(nums,m+1,r);  
    return root;  
}  
};
