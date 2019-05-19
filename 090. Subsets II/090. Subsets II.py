'''
在 Subsets 迭代版本的基础上思考。在迭代重复元素的时候会生成重复的结果，那么在迭代重复元素时要特殊处理一下。
就拿[1,2,2]来说，在迭代完1之后结果集为[[], [1]]，迭代第一个2后，[[], [1], [2], [1,2]]，接下来就要迭代重复的元素2了，
此时如果遍历在迭代第一个2之前就存在的结果集元素（[[], [1]]）时，就会产生重复，
我们只能在上一轮迭代产生的新的结果中继续添加。
所以要一个额外的变量来表示在结果集中的哪个位置开始遍历。
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        temp_size = 0
        for i in range(len(nums)):
            start = temp_size if i >= 1 and nums[i] == nums[i - 1] else 0
            temp_size = len(result)
            for j in range(start, temp_size):
                result.append(result[j] + [nums[i]])
        return result
