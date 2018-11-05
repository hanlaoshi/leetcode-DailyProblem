#欢迎关注微信公众号： AI数据分析算法
'''
解题思路
整体思路类似于在一个无序数组内找最小的k个数。
我们通过两个数组各自的中位数将两个数组A、B分为四个部分，
分别为A1、A2、B1、B2。现在我们来找出他们中第k小的数。
如果A的中位数比B的中位数大，那么B1中的数比A2和B2中的都小，且小于部分A1中的数。
此时，如果k>len(A1)+len(B1)，那么第k个数就不可能在B1，因为比B1的数小的数最多只有B1加上部分的A1，
也就是k<len(A1)+len(B1)，矛盾；同时，我们还知道了A2中的数比A1和B1的大，
且比部分B2的大，此时，如果k<=len(A1)+len(B1)，那么第k个数就不可能在A2中，
因为A2中的数至少比A1加B1中的数大,也就是k>len(A1)+len(B1)，矛盾。
同理可以推理出另外两种情况。
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        k = (length1 + length2) // 2
        if (length1 + length2) % 2 == 0:
            return (self.findK(nums1, nums2, k) + self.findK(nums1, nums2, k - 1)) / 2.0;   # 2 is enough in python3
        else:
            return self.findK(nums1, nums2, k)

    def findK(self, num1, num2, k):
        # Recursive ends here
        if not num1:
            return num2[k]
        if not num2:
            return num1[k]
        if k == 0:
            return min(num1[0], num2[0])

        length1 = len(num1)
        length2 = len(num2)
        if num1[length1 // 2] > num2[length2 // 2]:
            if k > length1 // 2 + length2 // 2:
                return self.findK(num1, num2[length2 // 2 + 1:], k - length2 // 2 - 1)
            else:
                return self.findK(num1[:length1 // 2], num2, k)
        else:
            if k > length1 // 2 + length2 // 2:
                return self.findK(num1[length1 // 2 + 1:], num2, k - length1 // 2 - 1)
            else:
                return self.findK(num1, num2[:length2 // 2], k)


if __name__ == "__main__":
    assert Solution().findMedianSortedArrays([1, 2], [1, 2, 3]) == 2
    assert Solution().findMedianSortedArrays([], [2, 3]) == 2.5
