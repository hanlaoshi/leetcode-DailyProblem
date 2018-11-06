------------------JAVA-----------------------
class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        int num = 0;
        for (int i = 0; i < nums.length; i++) {
            if(nums[num] != nums[i]){
                num++;
                nums[num] = nums[i];
            }
        }
        return ++num;
    }
}
