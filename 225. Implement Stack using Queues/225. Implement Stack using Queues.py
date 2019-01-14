'''
这题就是232的使用队列实现堆栈的反义了
队列是先进先出，每次出只能出队列的头部，而栈是后进先出，所以可以想办法每次把入队的元素弄到队列头部。于是可以考虑在每次push到队列的时候对其他元素做个重新pop和push将当前元素转移到队头。 
该方法需要一个队列，push的复杂度O(n)，pop的复杂度O(1)。
'''

#方法一
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.insert(0, x)
        for i in range(len(self.stack)-1):
            self.stack.insert(0, self.stack[-1])
            self.stack.pop()

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack




#方法二
'''
也可以用两个队列实现，将思路一的过程分开。但这时要引入一个变量来记录栈顶元素。 
该方法需要两个队列，push的复杂度O(1)，pop的复杂度O(n)。
'''
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.topx = None

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue1.insert(0, x)
        self.topx = x

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.queue1) > 1:
            self.topx = self.queue1.pop()
            self.queue2.insert(0, self.topx)
        self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1

    def top(self):
        """
        :rtype: int
        """
        return self.topx

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue1


'''
方法3 

用两个队列，push的复杂度O(n)，pop的复杂度O(1)。
'''
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue2.insert(0, x)
        while self.queue1:
            self.queue2.insert(0, self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue1.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.queue1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue1




