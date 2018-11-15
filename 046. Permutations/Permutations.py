'''
解题思路
这道题比较单间，采用递归把数组中的数字依次加入当前数组current来进行排列组合。

'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.get_permute([], nums, result)
        return result

    def get_permute(self, current, num, result):
        if not num:
            result.append(current + [])
            return
        for i, v in enumerate(num):
            current.append(num[i])
            self.get_permute(current, num[:i] + num[i + 1:], result)
            current.pop()


if __name__ == "__main__":
    assert Solution().permute([1, 2, 3]) 
