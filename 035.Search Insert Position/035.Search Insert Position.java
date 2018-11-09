public class Solution {
    public int searchInsert(int[] nums, int target) {
    	//特殊情况
        if(nums.length == 0 || nums[0] > target)
            return 0;
        if(nums[nums.length - 1] < target)
        	return nums.length;
        //先二分查找，找到了就返回
        int low = 0;
        int hight = nums.length - 1;
        int mid = 0;
        while(low <= hight){
            mid = (low + hight)/2;
            if(nums[mid] < target){
                low = mid + 1;
            }else if(nums[mid] > target){
                hight = mid - 1;
            }else{
                return mid;
            }
        }
        //找不到再判断与nums[mid]大小，返回索引
        return nums[mid] > target?mid:mid+1;
    }
}
