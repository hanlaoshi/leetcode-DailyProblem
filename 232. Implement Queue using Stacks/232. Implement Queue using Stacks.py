'''
这个题目的关键点在于，只能用栈的几个操作实现。 
由于栈先进后出，和队列先进先出天然矛盾，故考虑采用两个栈，一个只进行入栈push操作，
一个只进行出栈pop或peek操作。当只进行出栈操作的栈空时将另一个栈中的内容push到该栈，
如此，就拥有了先进先出的特性。
'''
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.inStack and not self.outStack
