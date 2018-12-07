#解题思路：
#这题要求你的算法时间复杂度必须是 O(log n) 级别。

#二分搜索法的关键在于获得了中间数后，判断下面要搜索左半段还是右半段，我们观察上面红色加粗的数字都是升序的，
#由此我们可以观察出规律，如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的，
#我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，这样就可以确定保留哪半边了，代码如下
class Solution {
public:
    int search(int A[], int n, int target) {
        if (n == 0) return -1;
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (A[mid] == target) return mid;
            else if (A[mid] < A[right]) {
                if (A[mid] < target && A[right] >= target) left = mid + 1;
                else right = mid - 1;
            } else {
                if (A[left] <= target && A[mid] > target) right = mid - 1;
                else left = mid + 1;
            }
        }
        return -1;
    }
};