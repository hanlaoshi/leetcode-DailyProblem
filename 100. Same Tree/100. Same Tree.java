//递归判断左右是否相等。

public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null&&q==null)
            return true;
        
        if(p==null&&q!=null)
            return false;
        
        if(p!=null&&q==null)
            return false;
            
        if(p.val!=q.val)
            return false;
        boolean isleftsame = isSameTree(p.left,q.left);
        if(!isleftsame)
            return false;
            
        boolean isrightsame = isSameTree(p.right,q.right);
        if(!isrightsame)
            return false;
        
        return true;
        
    }
    
    
/*
//另外一种更简洁的写法

public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null&&q == null)
            return true;
        if(p == null||q == null)
            return false;
        return (p.val == q.val) && isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
    }


*/

//第三种方法，by 三休大佬做法

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    boolean flag = true;
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null&& q==null)
            return true;
        if((p != null && q == null) || (p == null && q != null))
            return false;

        isSame(p,q);
        return flag;
    }
    
    
    public void isSame(TreeNode p,TreeNode q){
         if(p.val != q.val)
            flag = false;
        
        if ((p.left == null && q.left != null) || (p.left != null && q.left == null))
            flag = false;
        
        if (p.left != null && q.left != null)
            isSame(p.left,q.left);
        
        if((p.right == null && q.right != null) || (p.right != null && q.right==null))
            flag = false;

        if (p.right != null && q.right != null)
            isSame(p.right,q.right);
        
        
    }
}
