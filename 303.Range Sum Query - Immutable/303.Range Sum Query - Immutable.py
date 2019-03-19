class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [0]+nums
        for i in range(len(self.nums)):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j+1] - self.nums[i]