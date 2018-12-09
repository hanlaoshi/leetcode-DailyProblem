'''
方法一;

要求小于n的所有素数，一个高效的算法是“素数筛选法”。其思想是从小的素数开始，
排除该小素数的所有倍数，直到最终剩下的全是素数。具体的算法可以参考： 
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity

注意，方法一代码中的循环变量 i ，范围直到 sqrt(n)+1；循环变量 j，每次更新是 j=j+i。
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <3:
            return 0

        digits = [1]*n
        digits[0] = digits[1] = 0

        for i in xrange(2, int(n**0.5)+1):
            if digits[i] == 1:
                for j in xrange(i+i, n, i):
                    digits[j] = 0

        return sum(digits)


'''
方法二:

方法一的代码先求出所有素数，再进行计算总计多少个。一个简单的变体是在一遍遍历所有n个数的时候计算所有素数。
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <3:
            return 0

        digits = [0]*n
        count = 1
        sq = int(n**0.5)+1

        for i in xrange(3, n, 2):
            if not digits[i]:
                count += 1
                if i > sq:
                    continue
                for j in xrange(i+i, n, i):
                    digits[j] = 1

        return count
