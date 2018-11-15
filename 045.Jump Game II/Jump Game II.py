'''
解题思路
这是在 Jump Game 之上给出的问题，题目已经保证能够跳到最后。
遍历数组，起始到当前坐标所有跳跃方式能够到达的最远距离是reach，
我们跳n步能到达的最远距离用longest表示，如果longest不能到达当前坐标，
说明就要多跳一步了，直接跳到当前坐标之前的点能够跳到的最远位置。
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        counter = 0
        longest = 0
        reach = 0
        for i in range(length):
            if longest < i:
                counter += 1
                longest = reach
            reach = max(reach, nums[i] + i)
        return counter


if __name__ == "__main__":
    assert Solution().jump([2, 3, 1, 1, 4]) 
