
//这道题不算难题，就是使用一个哈希表，遍历整个数组，如果哈希表里存在，返回false，如果不存在，则将其放入哈希表中

//方法一
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            if (m.find(nums[i]) != m.end()) return true;
            ++m[nums[i]];
        }
        return false;
    }
};


// 方法二
//先将数组排个序，然后再比较相邻两个数字是否相等，时间复杂度取决于排序方法

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1]) return true;
        }
        return false;
    }
};

