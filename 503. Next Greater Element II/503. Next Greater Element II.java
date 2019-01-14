/*
这道题是之前那道Next Greater Element I的拓展，不同的是，此时数组是一个循环数组，
就是说某一个元素的下一个较大值可以在其前面，那么对于循环数组的遍历，为了使下标不超过数组的长度，
我们需要对n取余，下面先来看暴力破解的方法，遍历每一个数字，然后对于每一个遍历到的数字，遍历所有其他数字，注意不是遍历到数组末尾，
而是通过循环数组遍历其前一个数字，遇到较大值则存入结果res中，并break，再进行下一个数字的遍历
*/
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, -1);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < i + n; ++j) {
                if (nums[j % n] > nums[i]) {
                    res[i] = nums[j % n];
                    break;
                }
            }
        }
        return res;
    }
};


//解法二

/*
可以使用栈来进行优化上面的算法，我们遍历两倍的数组，然后还是坐标i对n取余，取出数字，
如果此时栈不为空，且栈顶元素小于当前数字，说明当前数字就是栈顶元素的右边第一个较大数，
那么建立二者的映射，并且去除当前栈顶元素，最后如果i小于n，则把i压入栈。
因为res的长度必须是n，超过n的部分我们只是为了给之前栈中的数字找较大值，所以不能压入栈，
*/

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, -1);
        stack<int> st;
        for (int i = 0; i < 2 * n; ++i) {
            int num = nums[i % n];
            while (!st.empty() && nums[st.top()] < num) {
                res[st.top()] = num; st.pop();
            }
            if (i < n) st.push(i);
        }
        return res;
    }
};
