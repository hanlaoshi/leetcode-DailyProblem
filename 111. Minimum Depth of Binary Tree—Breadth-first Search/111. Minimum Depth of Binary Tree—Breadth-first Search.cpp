//思路：
//！！！递归的终止条件：遍历到叶子结点，这里极容易错误的将遍历到节点为空作为递归终止条件，从而产生错误。

class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root == NULL)    //检测第一进入的时候给定的root是否为空
            return 0;
        if(root->left == NULL && root->right == NULL)   //递归终止条件
            return 1;
        int leftD = INT_MAX;    //左子树的最小深度（定义为最大值是为了min函数返回不为空的子树的深度+1）
        int rightD = INT_MAX;   //右子树的最小深度
        if(root->left != NULL)  //左子树为空，则返回右子树的深度+1
            leftD = minDepth(root->left);
        if(root->right != NULL) //右子树为空，则返回做子树的深度+1
            rightD = minDepth(root->right);
        return min(leftD, rightD) + 1;
    }
};
