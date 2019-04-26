//通过二叉树的前序遍历和中序遍历来构建二叉树，通过递归可以很容易的解决这个问题，在遇到二叉树的问题，应该习惯先画图再来解决
//原文：https://blog.csdn.net/u014265347/article/details/76400062

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int l1 = 0;
        int l2 = 0;
        int r1 = preorder.size() - 1;
        int r2 = inorder.size() - 1;
        TreeNode *s = (TreeNode*)malloc(sizeof(TreeNode));
        //s = NULL;
        s = CreateBT(preorder, inorder, l1, r1, l2, r2);
        return s;
    }

    TreeNode* CreateBT(vector<int>& preorder, vector<int>& inorder, int l1, int r1, int l2, int r2)
    {
        TreeNode* s;
        int i;
        if (l1 > r1)
            return NULL;
        s = (TreeNode*)malloc(sizeof(TreeNode));
        s->left = s->right = NULL;
        for (i = l2; i <= r2; i++)
        {
            if (inorder[i] == preorder[l1])
            {
                break;
            }
        }
        s->val = inorder[i];
        s->left = CreateBT(preorder, inorder, l1 + 1, l1 + i - l2, l2, i - 1);
        s->right = CreateBT(preorder, inorder, l1 + i - l2 + 1, r1, i + 1, r2);
        return s;
    }
};

