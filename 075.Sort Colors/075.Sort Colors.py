#--------------辰星-------------------
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return None
        bucket = {}
        for item in nums:
            bucket[item] = bucket.get(item, 0) + 1
        pos = 0
        for item in sorted(bucket.keys()):         
            limit = pos + bucket[item]            
            nums[pos:limit] = [item] * bucket[item]
            pos = limit