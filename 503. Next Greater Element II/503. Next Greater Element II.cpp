class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        const int N = nums.size();
        vector<int> res(N, -1);
        stack<int> stack;
        for (int i = 0; i < N * 2; i++) {
            while (!stack.empty() && nums[stack.top()] < nums[i % N]) {
                res[stack.top()] = nums[i % N];
                stack.pop();
            }
            if (i < N)
                stack.push(i);
        }
        return res;
    }
};
