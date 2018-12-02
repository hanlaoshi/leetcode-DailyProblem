class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>>v;
        stack<vector<int>>s;
        queue<TreeNode*>q;
        q.push(root);  //根节点入队
        if(root == NULL)  
            return v ;
        while(!q.empty()){  //队列不空
            vector<int>vv;
            queue<TreeNode*> next ;  //  建立第二个队列 用来存放下一层的结点
            
            while(!q.empty()){  //遍历每层的结点  这层循环是核心 其他都是为了满足OJ输出
                
                TreeNode* tre = q.front() ;
                vv.push_back(tre->val);  //访问该结点,为了满足输出要求，所以有点复杂，
                q.pop();  //对头元素出队
                if(tre->left!=NULL){  //它有左子树
                    next.push(tre->left);
                }
                if(tre->right!=NULL){  //它有右子树
                    next.push(tre->right);
                }
                
            }
            s.push(vv);  //将每层结点入栈
            //v.push_back(vv);
            q=next;  // // 遍历完后进入下一层 
        }
        while(!s.empty()){  //将每层结点倒序输出
            v.push_back(s.top());
            s.pop();
        }
        return v;
    }
};