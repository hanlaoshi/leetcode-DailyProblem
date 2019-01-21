class MovingAverage {
public:
    /** Initialize your data structure here. */
    MovingAverage(int size): len(size), sum(0) {
    }
    
    double next(int val) {
        sum += val;
        que.push(val);
        if(que.size() > len)
        {
            sum -= que.front();
            que.pop();
        }
        return sum/que.size();
    }
private:
    int len;
    double sum;
    queue<int> que;
};
 
/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
