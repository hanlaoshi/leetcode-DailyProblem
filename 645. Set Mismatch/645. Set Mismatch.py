'''
这个题明显使用hash的思想。把每个位置出现的次数统计一下，找出出现了2次和0次的数字的位置即可。
'''
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashs = [0] * len(nums)
        missing = -1
        for i in range(len(nums)):
            hashs[nums[i] - 1] += 1
        return [hashs.index(2) + 1, hashs.index(0) + 1]


'''
直接计算
和268. Missing Number很像，直接计算出来也可以，速度稍快点。
'''
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        nset = set(nums)
        missing = N * (N + 1) / 2 - sum(nset)
        duplicated = sum(nums) - sum(nset)
        return [duplicated, missing]
