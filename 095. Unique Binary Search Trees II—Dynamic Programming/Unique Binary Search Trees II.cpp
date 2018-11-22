class Solution {
public:
    
    vector<TreeNode*> generateTrees(int n) {
       vector<TreeNode*> t; 
       if(n==0)
       {
           return t;
       }
          
       return f(1,n);
};
    
    vector<TreeNode*> f(int l,int r)//递归建立左右子树
    {
       vector<TreeNode*> ans;
        
       if(l>r)
       {
           ans.push_back(NULL);
       }
       
       for(int k=l;k<=r;k++)//k为当前对应情况的根节点
       {
          vector<TreeNode*> left=f(l,k-1);
          vector<TreeNode*> right=f(k+1,r);
          
          for(int i=0;i<left.size();i++)//子树有多种组合的情况
          {
              for(int j=0;j<right.size();j++)
              {
                  TreeNode *temp=new TreeNode(k);
                  temp->left=left[i];
                  temp->right=right[j];
                  ans.push_back(temp);
              }
          }
       }
        
      return ans;
    }
};
