# 方法一，我们观察其中的一个位置，单独考虑这个位置的容量是多少？毫无疑问，我们只要知道，这个位置左边最高的那个边，和右边最高的那个边，两者取小的，然后再减去本身的大小，那么结果就是这个位置的容量。所以，
# （1）从左向右进行扫描，获取每个位置的左边最高的边。
# （2）从右向左进行扫描，获取每个位置的右边最高的边。
# （3）再遍历一边，计算出每个位置的容量，累加，即结果。

class Solution:
    def trap(self, height):
 
        if not height: return 0
        n, res = len(height), 0
        left_max, right_max = [0] * n, [0] * n
 
        left_max[0] = height[0]
        for i in range(1, n):  # 从左向右扫描一遍，求出每个位置左边最高的边
            left_max[i] = max(height[i], left_max[i - 1])
 
        right_max[n - 1] = height[n - 1]
        for i in range(n-2, -1, -1):  # 从右向左扫描一遍，求出每个位置右边最高的边
            right_max[i] = max(height[i], right_max[i + 1])
 
        for i in range(1, n-1):  # 扫描每一个位置，用当前位置左右最短的边，作为长度，并减去当前位置的值，就是当前位置的容量
            res += min(left_max[i], right_max[i]) - height[i]
        return res
 
 
if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solu = Solution()
    print(solu.trap(height))
# 方法二， 使用双指针法，在左右两端分别设置指针left, right，并且用 left_max， right_max 记录走过之后的最长最高的边。例如，left_max 就是指针left 左边最长的线，right_max 同理。
# （1）如果 height[left] < height[right]，就是左指针指向的数字 < 右指针指向的数字（现在操作左指针）,  说明此时，左边已经走过的位置都小于 height[right]，通俗的讲，现在left指针位置的左右两边桶的短板，一定存在于左边，又因为 left_max记录了当前left位置的左边最高的那个边，所以当前left位置的容量就是只需考虑left_max ， height[left] 这个两个值的大小即可得出。

# 问题：为什么说左边已经走过的位置都小于 height[right]？因为两个指针的移动条件是，那个指针小就移动那一个。

# （2）如果height[left] >= height[right]，同理（1）。直到两个指针相遇。

class Solution:
    def trap(self, height):
 
        if not height: return 0
        left_max = right_max = res = 0
        left, right = 0, len(height) - 1
 
        while left < right:
            if height[left] < height[right]:  # 左指针操作
                if height[left] < left_max:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1  # 移动左指针
            else:
                if height[right] < right_max:  # 右指针操作
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1  # 移动右指针
        return res
 
 
if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solu = Solution()
    print(solu.trap(height))
