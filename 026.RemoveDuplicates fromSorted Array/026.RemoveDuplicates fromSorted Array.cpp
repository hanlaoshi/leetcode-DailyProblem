#-----------CPP------------
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;

        int len;    //当前数组中已经筛选出的非重复元素个数
        len = 1;    //数组第一个元素直接计数
        for(int i = 1;i < nums.size();i++){
            if(nums[i] != nums[len - 1]){      //遍历到的非重复值               
                nums[len] = nums[i];            
                ++len;              
            }
        }
        return len;
    }
};
