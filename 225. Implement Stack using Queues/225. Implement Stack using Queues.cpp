class Stack {
public:
    queue<int> q, q2;

    // Push element x onto stack.
    void push(int x) {
        q.push(x);
    }

    // Removes the element on top of the stack.
    void pop() {
        if (q.size() == 1) q.pop();
        else {
            while (q.size() > 1) {
                q2.push(q.front());
                q.pop();
            }
            q.pop();
            while (q2.size() > 0) {
                q.push(q2.front());
                q2.pop();
            }
        }
    }

    // Get the top element.
    int top() {
        if (q.size() == 1) return q.front();
        while (q.size() > 1) {
            q2.push(q.front());
            q.pop();
        }
        int temp = q.front();
        q2.push(q.front());
        q.pop();
        while (q2.size() > 0) {
            q.push(q2.front());
            q2.pop();
        }
        return temp;
    }

    // Return whether the stack is empty.
    bool empty() {
        return q.empty();
    }
};


