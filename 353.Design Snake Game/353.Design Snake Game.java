public class SnakeGame {
    int m;
    int n;
    int[][] foods;
    Queue<Integer> queue;
    HashSet<Integer> set;
    int[] headPos;
    int foodSeq;


    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    public SnakeGame(int width, int height, int[][] food) {
        this.m = height;
        this.n = width;
        this.foods = food;
        this.queue = new LinkedList<Integer>();
        this.set = new HashSet<Integer>();
        this.headPos = new int[]{0, 0};
        this.foodSeq = 0;
        queue.offer(0);
        set.add(0);
    }
    
    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body. */
    public int move(String direction) {
        int[] dir;
        switch(direction) {
            case "U": dir = new int[]{-1, 0}; break;
            case "L": dir = new int[]{0, -1}; break;
            case "R": dir = new int[]{0, 1}; break;
            case "D": dir = new int[]{1, 0}; break;
            default: dir = new int[2];
        }
        int row = headPos[0] + dir[0]; // new position row
        int col = headPos[1] + dir[1]; // new position col
        
        //delete tail first, before push into a new cell
        if (foodSeq<foods.length && calcPosId(foods[foodSeq][0], foods[foodSeq][1]) == calcPosId(row, col)) {
            foodSeq++;
        }
        else {
            set.remove(queue.poll());
        }
        
        if (row<0 || row>=m || col<0 || col>=n) return -1; // hit border
        if (set.contains(calcPosId(row, col))) return -1; // hit its own body
        
        set.add(calcPosId(row, col));
        queue.offer(calcPosId(row, col));
        headPos[0] = row;
        headPos[1] = col;

        return set.size()-1;
    }
    
    public int calcPosId(int x, int y) {
        return x*n+y;
    }
}

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame obj = new SnakeGame(width, height, food);
 * int param_1 = obj.move(direction);
 */