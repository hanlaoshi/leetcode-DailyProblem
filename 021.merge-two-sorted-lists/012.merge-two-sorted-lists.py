#方法1：（python版本）
#为了避免分类讨论，添加一个假的头节点。现在只需要两个指针分别指向原来的两个链表，将其中比较小的节点添加到新的链表中。
#传入的参数l1和l2正好可以当作遍历两个链表的指针。

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode(-1)
        head = temp
        while l1 and l2:
            if l1.val > l2.val:
                temp.next = l2
                l2 = l2.next
            else:
                temp.next = l1
                l1 = l1.next
            temp = temp.next
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        return head.next


if __name__ == "__main__":
    assert Solution().mergeTwoLists(ListNode(1), ListNode(2)).val == 1
