'''
解题思路
顺序遍历所有节点，如果当前节点有后一个节点，且它们的值相等，那么当前节点指向后一个节点的下一个节点，这样就可以去掉重复的节点。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def my_print(self):
        print(self.val)
        if self.next:
            print(self.next.val)


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return head
