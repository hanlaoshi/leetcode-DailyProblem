#进行一遍遍历，把第m到n个元素进行翻转，即依次插入到第m个节点的头部。
#方法来源：https://blog.csdn.net/fuxuemingzhu/article/details/80794665 
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        root = ListNode(0)
        root.next = head
        pre = root
        while pre.next and count < m:
            pre = pre.next
            count += 1
        if count < m:
            return head
        mNode = pre.next
        curr = mNode.next
        while curr and count < n:
            next = curr.next
            curr.next = pre.next
            pre.next = curr
            mNode.next = next
            curr = next
            count += 1
        return root.next
