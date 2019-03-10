class MyCircularDeque {

    int[] queue;
    int front, rear, count;

    public MyCircularDeque(int k) {

        queue = new int[k];
    }

    public boolean insertFront(int value) {

        if (isFull())
            return false;
        front = front == 0 ? queue.length - 1 : front - 1;
        queue[front] = value;
        count++;
        return true;

    }

    public boolean insertLast(int value) {

        if (isFull())
            return false;
        queue[rear] = value;
        rear = (rear + 1) % queue.length;
        count++;
        return true;
    }

    public boolean deleteFront() {

        if (isEmpty())
            return false;
        front = (front + 1) % queue.length;
        count--;
        return true;
    }

    public boolean deleteLast() {

        if (isEmpty())
            return false;
        rear = rear == 0 ? queue.length - 1 : rear - 1;
        count--;
        return true;
    }

    public int getFront() {

        if (isEmpty())
            return -1;
        return queue[front];
    }

    public int getRear() {

        if (isEmpty())
            return -1;
        return rear == 0 ? queue[queue.length - 1] : queue[rear - 1];
    }

    public boolean isEmpty() {

        return count == 0;
    }

    public boolean isFull() {

        return count == queue.length;
    }
}