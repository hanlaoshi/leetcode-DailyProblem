----------- -用列表来维护队列中的元素值。---------------
class MyCircularQueue:
 
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.value = []
        
 
    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        #如果当前队列不是满的，就直接插入新元素
        if not self.isFull():
            self.value.append(value)
            return True
        #如果当前队列是满的，返回False
        else:
            return False
        
 
    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        #如果当前队列不是空的，就pop出第1个元素
        if not self.isEmpty():
            self.value.pop(0)
            return True
        else:
            return False
        
       
    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.value[0]
        
 
    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        
        if self.isEmpty():
            return -1
        else:
            return self.value[-1]
        
 
    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if len(self.value) == 0:
            return True
        else:
            return False
 
    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.size == len(self.value):
            return True
        else:
            return False
        
 
 
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
