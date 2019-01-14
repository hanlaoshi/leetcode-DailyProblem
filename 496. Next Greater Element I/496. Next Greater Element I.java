public class Solution {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {
        if(findNums == null ||  nums == null || 
           findNums.length == 0 || nums.length == 0 || 
           findNums.length > nums.length) return new int[0];

        int m = findNums.length;
        int n = nums.length;
        int[] result = new int[m];
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int j = 0; j < n; ++j){
            map.put(nums[j], j);
        }
        for(int i = 0; i < m; ++i){
            int j = map.get(findNums[i]);
            for(; j < n; ++j){
                if(nums[j] > findNums[i]) break;
            }
            result[i] = j < n ? nums[j] : -1;
        }
        return result;
    }
}


//解法二 ，leetcode牛方法

'''
重点观察： 假设我们有一个递减的序列，后跟一个更大的数字 例如[5,4,3,2,1,6]，则数字6越大，序列中所有先前数字的下一个更大元素 
我们使用一个堆栈来保持一个递减的子序列，每当我们看到一个数字x大于stack.peek（）时我们弹出所有小于x的元素，对于所有弹出的元素，
它们的下一个更大的元素是x 例如[9,8,7,3,2,1,6] 堆栈首先包含[9,8,7,3,2,1]，然后我们看到6大于1所以我们弹出1 2 3，
其下一个更大的元素应该是6
'''
public int[] nextGreaterElement(int[] findNums, int[] nums) {
    Map<Integer, Integer> map = new HashMap<>(); // map from x to next greater element of x
    Stack<Integer> stack = new Stack<>();
    for (int num : nums) {
        while (!stack.isEmpty() && stack.peek() < num)
            map.put(stack.pop(), num);
        stack.push(num);
    }   
    for (int i = 0; i < findNums.length; i++)
        findNums[i] = map.getOrDefault(findNums[i], -1);
    return findNums;
}

