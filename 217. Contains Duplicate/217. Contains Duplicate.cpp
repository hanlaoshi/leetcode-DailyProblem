/*
思路分析：

方法一：

判断数组中的数是否重复，有重复返回true。无重复返回false。

遍历数组，将数组中的数存储到set中，每次插入nums[ i ]之前判断是否已在set中存在，如果已经存在，说明存在重复，返回true。

时间复杂度：O(n)

空间复杂度：O(n)

*/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        //遍历数组，查看数组中的数是否在set中，如果不在，将数组中的数存储到set中，如果在，有重复，返回false
        if(nums.size() == 0) return false;
        if(nums.size() == 1) return false;
        
        set<int> cpnums;
        for(int i = 0; i < nums.size(); i ++){
            if(cpnums.find(nums[i]) != cpnums.end())
                return true;
            else{
                cpnums.insert(nums[i]);
            }
        }
        return false;
    }
};


/*
方法二：

可以先将数组排序，然后判断相邻的两个数是否有相等的，有，说明有重复，返回true。

时间复杂度：O(n)

空间复杂度：O(1)

*/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for(int i = 1; i < nums.size(); i ++){
            if(nums[i] == nums[i - 1])
                return true;
        }
        return false;
    }
};
