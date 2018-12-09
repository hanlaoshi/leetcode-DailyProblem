class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    assert Solution().containsDuplicate([1, 2, 3, 4]) == False
    assert Solution().containsDuplicate([1, 2, 3, 1]) == True
