#     def __init__(self, x):
#         self.val = x
#         self.next = None
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        add = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        head = ListNode(add[0])
        print(head)
        answer = head
        for i in range(1, len(add)):
            node = ListNode(add[i])
            head.next = node
            head = head.next
        return answer

if __name__ == "__main__":
        # 创建对象Solution
    sol = Solution()
    # 定义l1链表
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(5)
    # 定义l2链表
    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)
    # 获取返回值的链表
    res = sol.addTwoNumbers(l1, l2)
    # 循环遍历出来
    while res:
        print(res.val)
        res = res.next


'''
还有一种是leetcode官网解法

'''

'''
根据官方solution的方法，可以采用一个进位carry方便的完成一次遍历得出结果，不过过程稍微麻烦。



两个要注意的地方：如果列表长度不相等；如果列表相加完成最后仍有进位位。

'''

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        answer = head
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add % 10)
            head = head.next
            l1, l2 = l1.next, l2.next
        l = l1 if l1 else l2
        while l:
            add = l.val + carry
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add % 10)
            head = head.next
            l = l.next
        if carry:
            head.next = ListNode(1)
        return answer.next
if __name__ == "__main__":
        # 创建对象Solution
    sol = Solution()
    # 定义l1链表
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(5)
    # 定义l2链表
    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)
    # 获取返回值的链表
    res = sol.addTwoNumbers(l1, l2)
    # 循环遍历出来
    while res:
        print(res.val)
        res = res.next


'''
