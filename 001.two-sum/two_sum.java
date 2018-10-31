public class Solution {
  public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> m = new HashMap<Integer, Integer>();
    int[] res = new int[2];
    for (int i = 0; i < nums.length; ++i) {
      m.put(nums[i], i);
    }
    for (int i = 0; i < nums.length; ++i) {
      int t = target - nums[i];
      if (m.containsKey(t) && m.get(t) != i) {
        res[0] = i;
        res[1] = m.get(t);
        break;
      }
    }
    return res;
  }
}
