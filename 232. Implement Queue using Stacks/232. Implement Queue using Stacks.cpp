class Queue {
public:
    // Push element x to the back of queue.
    void push(int x) {
        stack<int> tmp;
        while (!s.empty()) {
            tmp.push(s.top());
            s.pop();
        }
        s.push(x);
        while (!tmp.empty()) {
            s.push(tmp.top());
            tmp.pop();
        }
    }
 
    // Removes the element from in front of queue.
    void pop(void) {
        s.pop();
    }
 
    // Get the front element.
    int peek(void) {
        return s.top();
    }
 
    // Return whether the queue is empty.
    bool empty(void) {
        return s.empty();
    }
 
private:
    stack<int> s;
};
