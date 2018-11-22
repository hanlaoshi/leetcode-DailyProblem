题解：
是Unique Binary Search Trees的进阶版本. 返回的不是个数，而是每一个结果。

对于i在[1,n]区间内, 以i为root时, 生成BST的left child 是由1到i-1生成的, BST的right child 是由i+1 到n生成的.

recursive call先得到左右子树分别的所有结果.

然后从左右子树的返回结果中依次取点，接到有 i 生成的root上，一共有m*n种接法。构造好后当前root加到res里.

recursive call的 stop condition是l>r. 此时没有i能存在[l, r]这个区间内. 加上null节点.

可行的BST数量是卡特兰数，不是多项式时间，所以要求解所有结果也不是在多项式时间内可以完成的。

Time Complexity: O(catalan number), exponential.

Space: O(n). 开了n层stack.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<TreeNode> generateTrees(int n) {
        List<TreeNode> res = new ArrayList<TreeNode>();
        if(n<1){
            return res;
        }
        
        return helper(1,n);
    }
    
    private List<TreeNode> helper(int left, int right){
        List<TreeNode> res = new ArrayList<TreeNode>();
        if(left > right){
            res.add(null);
            return res;
        }
        
        for(int i = left; i<=right; i++){
            List<TreeNode> leftRes = helper(left,i-1);
            List<TreeNode> rightRes = helper(i+1, right);
            //从leftRes中挨个取结果，配合从rightRes中挨个取结果后分别放在以i为root的左右子树上
            for(int m = 0; m<leftRes.size(); m++){
                for(int n = 0; n<rightRes.size(); n++){
                    TreeNode root = new TreeNode(i);
                    root.left = leftRes.get(m);
                    root.right = rightRes.get(n);
                    res.add(root);
                }
            }
        }
        return res;
    }
}