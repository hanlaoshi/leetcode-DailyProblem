public class MovingAverage {

    ArrayList<Integer> queue;
    int queue_size; 
    double sum;
    /** Initialize your data structure here. */
    public MovingAverage(int size) 
    {
        queue = new ArrayList<>(size);
        queue_size = size;
        sum = 0;
    }
    
    public double next(int val) 
    {
        if(queue.size() == queue_size) // meaning it is full
        {
            sum -= queue.get(0); // minus head
            queue.remove(0); // remove the head
        }
        
        queue.add(val); //append the new integer
        sum += val; // add into sum
        
        return (sum / queue.size());    
    }
}
#---------------------2---------------------------------
/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
public class MovingAverage {
    private int[] vals;
    private int from, size;
    private long sum;
 
    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        this.vals = new int[size];
    }
    
    public double next(int val) {
        if (size < vals.length) {
            sum += val;
            vals[size++] = val;
        } else {
            sum -= vals[from];
            vals[from] = val;
            from = (from+1) % vals.length;
        }
        return (double)sum / size;
    }
}
 
/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
