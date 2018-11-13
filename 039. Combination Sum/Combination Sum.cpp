/*
因为我们可以任意组合任意多个数，看其和是否是目标数，而且还要返回所有可能的组合，
所以我们必须遍历所有可能性才能求解。为了避免重复遍历，我们搜索的时候只搜索当前或之后的数，
而不再搜索前面的数。因为我们先将较小的数计算完，
所以到较大的数时我们就不用再考虑有较小的数的情况了。
这题是非常基本且典型的深度优先搜索并返回路径的题。

*/

public class Solution {
    
    List<List<Integer>> res;
    
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        res = new LinkedList<List<Integer>>();
        List<Integer> tmp = new LinkedList<Integer>();
        // 先将数组排序避免重复搜素
        Arrays.sort(candidates);
        helper(candidates, target, 0, tmp);
        return res;
    }
    
    private void helper(int[] nums, int target, int index, List<Integer> tmp){
        // 如果当前和已经大于目标，说明该路径错误 
        if(target < 0){
            return;
        // 如果当前和等于目标，说明这是一条正确路径，记录该路径
        } else if(target == 0){
            List<Integer> oneComb = new LinkedList<Integer>(tmp);
            res.add(oneComb);
        // 否则，对剩余所有可能性进行深度优先搜索
        } else {
            // 选取之后的每个数字都是一种可能性
            for(int i = index; i < nums.length; i++){
                // 典型的先加入元素，再进行搜索，递归回来再移出元素的DFS解法 
                tmp.add(nums[i]);
                helper(nums, target - nums[i], i, tmp);
                tmp.remove(tmp.size() - 1);
            }
        }
    }
}
