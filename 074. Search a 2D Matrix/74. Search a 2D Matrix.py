class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 首先判断二维数组的行数和列数是否为0，也就是判断这个二维数组是否为空数组
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        # 定义行数和列数
        hang = len(matrix)
        lie = len(matrix[0])
        # 按照下标来判断每个数字在数组中的位置，arr【0】【0】的下标为0。arr【hang】【lie】的下标是hang * lie - 1
        start, end = 0, hang * lie - 1
        '''以下判断的是行数列数大于1的情况'''
        # 使用while循环来遍历二维数组，使用二分查找的思想，先找到中间值，然后判断中间值和target的大小.
        # mid // lie表示的是中间值的行坐标，mid % lie表示的是中间值的列坐标
        '''
        如果中间值=target，返回true
        如果中间值>target，根据有序数组可知，target有可能出现在start到mid之间，因此将end变成mid，继续二分查找
        如果中间值<target，根据有序数组可知，target有可能出现在mid到end之间，因此将start变成mid，继续二分查找
        '''
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid // lie][mid % lie] > target:
                end = mid
            elif matrix[mid // lie][mid % lie] < target:
                start = mid
            else:
                return True
        '''以下判断的是行数大于1，列数等于1的情况'''
        if matrix[start // lie][start % lie] == target:
            return True
        '''以下判断的是列数大于1，行数等于1的情况'''
        if matrix[end // lie][end % lie] == target:
            return True
        # 凡是不满足以上的条件就返回false
        return False
 
 
sl = Solution()
print(sl.searchMatrix( [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]], 5))
print(sl.searchMatrix( [[1,   3,  5,  7]], 7))
print(sl.searchMatrix( [[1],[9],[23]], 9))
