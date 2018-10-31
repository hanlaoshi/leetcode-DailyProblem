class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        逼近法 
        每次左右两端都舍去短的那一端 
        若选择短的那一端【S=小于等于此端的高*小于等于当前的最大区间长度】
        至多的面积也是选择最左最右的一个矩形，因此不必再考虑短的一端，直接舍去逼近
        """
        # 记录当前最大容量的面积
        max_area = 0
        # 记录最左边的下标
        left = 0
        # 记录右边的下标
        right = len(height) - 1
        # 当右边下标大于左边下标的时候循环
        while right > left:
            # 当前循环中最大的容量面积，使用max方法比较上次的max_area和此次的容量面积，取最大值
            # min(height[left], height[right]) * (right - left) 取左边和右边的高当中的最小值， 下标right-left为宽，两者相乘为最大面积
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            # 判断哪条高小，小的那边下标进行操作
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_area
