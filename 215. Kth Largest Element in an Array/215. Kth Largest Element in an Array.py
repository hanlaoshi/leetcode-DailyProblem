#解题思路：利用快速排序的思想。每次找一半。最坏情况O(N2)，平均时间O(N)。
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.find(nums,k-1,0,len(nums)-1)
    def find(self,nums,k,left,right):
        l = left
        r = right
        partition = nums[(left+right)/2]
        while(left<=right):#结束条件是left大于right，否则有可能需要交换
            while(nums[left]>partition):
                left += 1
            while(nums[right]<partition):
                right -= 1
            if left <= right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        if right >= k and right>l:
            #说明在右半边
            return self.find(nums,k,l,right)
        if left <= k and left<r:
            #说明在左半边
            return self.find(nums,k,left,r)
        #nums[k]已经是第k+1大的数
        return nums[k]
