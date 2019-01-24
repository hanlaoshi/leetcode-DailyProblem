class MyCircularQueue {
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        data.resize(k);
        head = 0;
        tail = 0;
        reset = true;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if (isFull()) return false;
        // update the reset value when first enqueue happens
        if (head == tail && reset) reset = false;
        data[tail] = value;
        tail = (tail + 1) % data.size();
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % data.size();
        // update the reset value when last dequeue happens
        if (head == tail && !reset) reset = true; 
        return true;
    }
    
    /** Get the front item from the queue. */
    int Front() {
        if (isEmpty()) return -1;
        return data[head];
    }
    
    /** Get the last item from the queue. */
    int Rear() {
        if (isEmpty()) return -1;
        return data[(tail + data.size() - 1) % data.size()];
    }
    
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        if (tail == head && reset) return true;
        return false;
    }
    
    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        if (tail == head && !reset) return true;
        return false;
    }
private:
    vector<int> data;
    int head;
    int tail;
    // reset is the mark when the queue is empty
    // to differentiate from queue is full
    // because in both conditions (tail == head) stands
    bool reset;
};
