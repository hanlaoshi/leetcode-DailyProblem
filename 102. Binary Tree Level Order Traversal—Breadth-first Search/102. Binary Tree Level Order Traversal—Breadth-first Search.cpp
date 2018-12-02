class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        
        if (root == nullptr) {
            return result;
        }
        
        std::list<TreeNode*> temp;
        temp.push_back(root);

        while (temp.size() != 0) {
            vector<int> level;
            int size = temp.size();
            for(int i = 0; i < size; i++) {
               TreeNode *node = temp.front();               
               level.push_back(node->val);
               
               if (node->left) temp.push_back(node->left);
               if (node->right) temp.push_back(node->right);
                
                temp.pop_front();
            }

            result.push_back(level);
        }
        
        return result;
    }
};