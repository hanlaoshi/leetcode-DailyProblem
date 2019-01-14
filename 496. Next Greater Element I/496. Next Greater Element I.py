'''
直接遍历查找
想法比较淳朴：先从nums2中找到对应的nums1数值的序号，然后从这个序号往又找，看有没有比nums1数字大的。

如果有，把这个数字放到结果里；如果没有，就把-1放到结果里。
'''

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for num1 in findNums:
            index = -1
            for i,nums2 in enumerate(nums):
                if num1 == nums[i]:
                    index = i
                    break
            while index < len(nums) and num1 >= nums[index]:
                index += 1
            if index == len(nums):
                answer.append(-1)
            else:
                answer.append(nums[index])            
        return answer
