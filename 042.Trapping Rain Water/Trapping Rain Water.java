    //双指针 不使用堆栈
    public int trap3(int[] height) {
        int length = height.length;
        if(length<=2){
            return 0;
        }
        
        //获得可以盛水的区间
        int startIndex = 0;
        while(startIndex<length-1 && height[startIndex]<=height[startIndex+1]){
            startIndex++;
        }
        
        int result = 0;
        
        //这里思路类似于上一段代码，只是可以填水的区间将值改为填水后的值
        int index = startIndex;
        while(++index < length){
            int currentHeight = height[index];
            if(currentHeight > height[startIndex]){
                for(int i = index-1 ; i > startIndex ; i--){
                    result += (height[startIndex] - height[i]);
                }
                startIndex = index;
            }else{
                for(int i = index ; i>0 && height[i] > height[i-1] ; i--){
                    result += (height[i] - height[i-1]);
                    height[i-1] = height[i];
                }
            }
        }
        return result;
    }
//思路二：动态编程 先遍历获得区间左右最大值再计算
// 思路一中，每一次对一个区间都要遍历整个数组才能获得左右最大值。
// 但是其实，从左往右遍历一次数组，可以获得各个区间的leftMax。
// 同理，从右往左遍历可以获得各个区间的rightMax。将这两个值都存在数组中，并对数组进行遍历，计算各个区间的盛水高度。时间复杂度为O(n),代码如下：
    public int trap3(int[] height){
        int length = height.length;
        //leftMax数组
        int[] left = new int[length];
        //rightMax数组
        int[] right = new int[length];
        
        int leftMax = 0;
        int rightMax = 0;
        for(int i = 0 ; i<length ; i++){
            leftMax = left[i] = Math.max(leftMax,    height[i]);
            rightMax = right[length-i-1] = Math.max(rightMax, height[length-i-1]);
        }
        int result = 0;
        for(int j = 0 ; j<length ; j++){
            result += Math.min(left[j], right[j]) - height[j];
        }
        return result;
    }
//思路三：堆栈的聪明使用
//在这里，堆栈允许我们渐进的通过横向分割而非之前传统的纵向分割的方式来累加计算盛水量。一旦当前区间的高度超过栈顶的元素，
//就代表栈顶元素有一个右边界。鉴于栈中的元素都是递减的，所以如果存在一个比栈顶元素大的栈中元素，则一定可以确定该区间的盛水量。代码如下：
    public int trap4(int[] height){
        int length = height.length;
        int result = 0, current = 0;
        
        Stack<Integer> s = new Stack<Integer>();
        
        while(current < length){
            while(!s.isEmpty() && height[current] > height[s.peek()]){
                int top = s.pop();
                if(s.isEmpty()){
                    break;
                }
                //获得两个节点之间的宽度
                int distance = current - s.peek() - 1;
                int tempHeight = Math.min(height[current], height[s.peek()]) - height[top];
                result += tempHeight  * distance;
            }
            s.push(current++);
        }
        return result;
    }
//思路四：双指针的进阶
    public int trap5(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int result = 0;
        int leftMax=0, rightMax=0;
        while(left < right){
            if(height[left] < height[right]){
                leftMax = Math.max(height[left], leftMax);
                result += leftMax - height[left];
                left++;
            }else{
                rightMax = Math.max(height[right], rightMax);
                result += rightMax - height[right];
                right--;
            }
        }
        return result;
    }