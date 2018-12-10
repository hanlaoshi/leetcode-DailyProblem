
百度面试题，有一个数组，先严格升序，后严格降序，eg 1 3 5 4 2，找出最大的数

可以参考leet 852题

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int l = 0, r = A.size() - 1;
        while (l <= r) {
            int mid = (l + r) >> 1;
            if (A[mid] > A[mid - 1] && A[mid] > A[mid + 1]) return mid;
            else if (A[mid] > A[mid - 1] && A[mid] < A[mid + 1]) l = mid + 1;
            else r = mid - 1;
        } 
        return -1;
    }
};
