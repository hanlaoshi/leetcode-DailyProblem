-------------PYTHON----------------
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        s = 0
        for f in range(1, len(nums)):
            if nums[s] != nums[f]:
                s += 1
                nums[s] = nums[f]
        return s + 1
