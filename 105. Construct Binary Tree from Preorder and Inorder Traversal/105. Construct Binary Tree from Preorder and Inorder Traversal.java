/**
方法来源：https://blog.csdn.net/buppt/article/details/78998568
首先我们要知道前序遍历是先访问根节点，再访问左子树，再访问右子树。中序遍历先访问左子树，再访问根节点，最后访问右子树。

例如一棵树如下：

       A
   B       C
 D   E   F   G
1
2
3
前序遍历结果是A BDE CFG 
中序遍历结果是DBE A FCG

我用空格分开了根节点、左子树和右子树。然后我们可以发现规律：

前序遍历的第一个节点是根节点，然后可以根据前序遍历和中序遍历找到左子树和右子树，然后递归分别求左子树和右子树的子树根节点即可。


*/
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> inMap = new HashMap<Integer, Integer>();//这里用hashmap比循环找要快。
        for(int i=0;i<inorder.length;i++){
            inMap.put(inorder[i],i);
        }
        return build(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1, inMap);
    }
    public TreeNode build(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd, Map<Integer, Integer> inMap){
        if(preStart>preEnd||inStart>inEnd){
            return null;
        }
        //前序遍历的第一个节点即该子树的根节点。
        TreeNode root=new TreeNode(preorder[preStart]);
        int inRoot=inMap.get(root.val);
        int numsLeft=inRoot - inStart;
        //然后我们就可以知道两个子树的起点和终点
        root.left = build(preorder, preStart + 1, preStart + numsLeft, inorder, inStart, inRoot - 1, inMap);
        root.right = build(preorder, preStart + numsLeft + 1, preEnd, inorder, inRoot + 1, inEnd, inMap);
        return root;
    }
}
