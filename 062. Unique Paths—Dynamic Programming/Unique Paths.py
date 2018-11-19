#----------------------python(辰星出品)--------------------
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def recursion_paths(x, y):
            n = 0
            if x:
                n += recursion_paths(x - 1, y)

            if y:
                n += recursion_paths(x, y - 1)              
            if x == 0 and y == 0:
                n = 1
            return n

        return recursion_paths(m - 1, n - 1)
