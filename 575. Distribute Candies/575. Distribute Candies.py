'''
思路
这题换一个表达方式就是：一个数组，划分为元素个数相等的两份，使得其中一份中元素的值尽可能不相同。

这里一个关键点在于“不同值的个数”和“子数组长度”的关系。例如[1, 2, 3, 4]的“不同值的个数”是4，“子数组长度”是2，很显然无论如何划分都是最优解（如[1, 2]），即2；再例如[1, 1, 2, 2, 2, 2]的“不同值的个数”是2，“子数组长度”是3，最优的划分是[1, 1, 2]或[1, 2, 2]，即2。

这样答案就呼之欲出了：“不同值的个数” > “子数组长度” ? “子数组长度” : “不同值的个数”。
'''

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        nums = set(candies)
        num_nums = len(nums)
        target_num = len(candies) // 2
        return target_num if num_nums >= target_num else num_nums
