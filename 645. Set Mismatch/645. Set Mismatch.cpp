
// 最直接的一种解法就是统计每个数字出现的次数了，然后再遍历次数数组，如果某个数字出现了两次就是重复数，如果出现了0次，就是缺失数

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> res(2, 0), cnt(nums.size(), 0);
        for (int num : nums) ++cnt[num - 1];
        for (int i = 0; i < cnt.size(); ++i) {
            if (res[0] != 0 && res[1] != 0) return res;
            if (cnt[i] == 2) res[0] = i + 1;
            else if (cnt[i] == 0) res[1] = i + 1;
        }
        return res;
    }
};


/*
再来看一种更省空间的解法，这种解法思路相当巧妙，遍历每个数字，然后将其应该出现的位置上的数字变为其相反数，
这样如果我们再变为其相反数之前已经成负数了，说明该数字是重复数，
将其将入结果res中，然后再遍历原数组，如果某个位置上的数字为正数，说明该位置对应的数字没有出现过，加入res中即可

*/

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> res(2, -1);
        for (int i : nums) {
            if (nums[abs(i) - 1] < 0) res[0] = abs(i);
            else nums[abs(i) - 1] *= -1;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) res[1] = i + 1;
        }
        return res;
    }
};
