题目：
设计实现双端队列。
你的实现需要支持以下操作：
MyCircularDeque(k)：构造函数,双端队列的大小为k。
insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
isEmpty()：检查双端队列是否为空。
isFull()：检查双端队列是否满了。
class MyCircularDeque:
    queue = []
    count, front, rear = 0, 0, 0

    def __init__(self, k):
        self.queue = [0 for i in range(k)]

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = len(self.queue) - 1 if self.front == 0 else self.front - 1
        self.queue[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % len(self.queue)
        self.count += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.queue)
        self.count -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = len(self.queue) - 1 if self.rear == 0 else self.rear - 1
        self.count -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[len(self.queue) - 1] if self.rear == 0 else self.queue[self.rear - 1]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.queue)