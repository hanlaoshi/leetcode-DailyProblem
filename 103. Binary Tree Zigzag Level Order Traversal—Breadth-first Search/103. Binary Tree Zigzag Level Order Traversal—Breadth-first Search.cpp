class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>ans;
        if(root==NULL)return ans;
        queue<TreeNode *>q;
        q.push(root);
        int flag=1;
        while(!q.empty()){
            queue<TreeNode *>qt;
            vector<int>res;
            while(!q.empty()){
                TreeNode *t=q.front();q.pop();
                res.push_back(t->val);
                if(t->left)qt.push(t->left);
                if(t->right)qt.push(t->right);
            }
            if(flag<0)reverse(res.begin(),res.end());
            flag=-flag;//标志是否需要反转
            ans.push_back(res);
            q=qt;
        }
        return ans;
    }
};
