Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

将两个有序数组合并成为一个。
注意点：

第一个数组有充足的空间来存放第二个数组中的元素
第一个数组的有效长度为m，第二个的有效长度为n
在原数组上修改，没有返回值
例子：

输入: nums1 = [1, 1, 2, 2, 4, 0, 0, 0, 0], m = 5, nums2 = [0, 0, 2, 3], n = 4
输出: 无（nums1变为[0, 0, 1, 1, 2, 2, 2, 3, 4]）
