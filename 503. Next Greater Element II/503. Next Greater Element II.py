#直接使用暴力解法的话。可以使用%符号来实现循环数组。可惜超时了。
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        _len = len(nums)
        res = [-1] * _len
        for i in xrange(_len):
            for j in xrange(i + 1, _len * 2):
                if nums[j % _len] > nums[i]:
                    res[i] = nums[j % _len]
                    break
        return res


#另寻他法   使用单调递减栈  

'''
在遍历数组的过程中，如果是往后遇到大的数，那就是第一个更大的数，
如果一直遇到不断小的数，才会一直找不到，我们可以用一个栈来记录，
遇到比栈顶小的数字就放入栈中，遇到比栈顶大的数字就说明这是栈顶数字的下一个更大的数，
就将其放在结果数组的对应位置上，栈顶的元素出栈，继续比较新的栈顶的数，如果还是大，
那么继续记录，出栈，直到栈顶的数比新数要小，那么就可以将新数入栈了。
因为我们要将找到的更大的数放在对应位置上，所以栈中记录的应该是元素位置，而不是具体的数字，
但比较的时候还是比较原来的数组中这个位置的数字，这一点要想清楚。此外，因为会出现循环寻找的情况，
所以数组我们可能遍历两次。这个做法会快很多。

注意，栈里保存的是索引!!!

同样适用单调栈的题目有：962. Maximum Width Ramp

'''
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        stack = []
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
