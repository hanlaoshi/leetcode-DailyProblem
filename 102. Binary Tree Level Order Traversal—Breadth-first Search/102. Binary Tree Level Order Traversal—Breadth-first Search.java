
//与树的前中后序遍历的DFS思想不同，层次遍历用到的是BFS思想。一般DFS用递归去实现（也可以用栈实现），BFS需要用队列去实现。

//层次遍历的步骤是：

//1.对于不为空的结点，先把该结点加入到队列中

//2.从队中拿出结点，如果该结点的左右结点不为空，就分别把左右结点加入到队列中

//3.重复以上操作直到队列为空

 public class Solution{
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
public static void LaywerTraversal(TreeNode root){
        if(root==null) return;
        LinkedList<TreeNode> list = new LinkedList<TreeNode>();  
        list.add(root);
        TreeNode currentNode;
        while(!list.isEmpty()){
            currentNode=list.poll();
            System.out.println(currentNode.val);
            if(currentNode.left!=null){
                list.add(currentNode.left);
            }
            if(currentNode.right!=null){
                list.add(currentNode.right);
            }
        }
    }
}