
class Solution {
public:
    vector<int> grayCode(int n) {
        if (n == 0) return {0};
        if (n == 1) return {0, 1};
        vector<int> res;
        vector<int> pre = grayCode(n - 1);
        for (int p : pre) {
            res.push_back(p);
        }
        for (auto p = pre.rbegin(); p < pre.rend(); p++) {
            res.push_back((1 << (n - 1)) + *p);
        }
        return res;
    }
};
