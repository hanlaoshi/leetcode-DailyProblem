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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        travel(root,result,0);
        return result;
    }
    public void travel(TreeNode root, List<List<Integer>> result, int level){
        if(root == null){
            return;
        }
        if(result.size() <= level){
            List<Integer> newLevel = new LinkedList<>();
            result.add(newLevel);
        }
        List<Integer> collection  = result.get(level);
        if(level % 2 == 0) collection.add(root.val);
        else collection.add(0, root.val);
        travel(root.left, result, level+1);
        travel(root.right, result, level+1);
        
        
    }
}