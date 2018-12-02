class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result=[]
        stackNode=[root]
        while stackNode:
            currentNode,temp=[],[]
            for i in stackNode:
                temp.append(i.val)
                
                if i.left:
                    currentNode.append(i.left)
                if i.right:
                    currentNode.append(i.right)
            stackNode=currentNode
            result.append(temp)
        return result