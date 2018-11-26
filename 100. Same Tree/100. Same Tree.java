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
