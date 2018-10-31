//方法4（leetcode版）：逼近法
//每次左右两端都舍去短的那一端 
//若选择短的那一端【S=小于等于此端的高*小于等于当前的最大区间长度】，至多的面积也是选择最左最右的一个矩形，因此不必再考虑短的一端，直接舍去逼近

class Solution {
public:
    int maxArea(vector<int>& height) {
    int _m = 0, r = height.size()-1,l=0;
    while (r > l) {
        _m = max(_m, min(height[l], height[r])*(r - l));
        if (height[r] > height[l]) ++l;
        else --r;
    }
    return _m;
    }
};
