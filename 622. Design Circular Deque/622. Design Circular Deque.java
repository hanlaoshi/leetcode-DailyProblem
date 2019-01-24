public class MyCircularQueue {
    public int count;
    public int[] data;
    public int head;
    public int tail; 
    public int length;
    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        count=0;
        head=0;
        tail=0;
        length=k;
        data=new int[k];
    }

    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public bool EnQueue(int value) {
        if(IsFull()) 
            return false;
        data[tail]=value;
        tail=(tail+1)%length;
        count++;
        return true;
    }

    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public bool DeQueue() {
        if(IsEmpty())
            return false;
        head=(head+1)%length;
        count--;
        return true;
    }

    /** Get the front item from the queue. */
    public int Front() {
        if(IsEmpty())
            return -1;
        return data[head];
    }

    /** Get the last item from the queue. */
    public int Rear() {
        if(IsEmpty())
            return -1;
        return tail==0?data[length-1]:data[(tail-1)%length];
    }

    /** Checks whether the circular queue is empty or not. */
    public bool IsEmpty() {
        return count==0;
    }

    /** Checks whether the circular queue is full or not. */
    public bool IsFull() {
        return count==length;
    }
}