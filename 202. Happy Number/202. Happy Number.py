'''
思路：
按照“happy number”的定义，直接循环计算各位平方和，观察是否收敛到1，若是则是 happy number。
为了判断循环是否开始重复，要用一个字典（dict）或集合（set）来保存已经出现的数字，dict的效率更高。

'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_dict = {}

        while True:
            num_dict[n] = True
            sum = 0
            while(n>0):
                sum += (n%10)*(n%10)
                n /= 10
            if sum == 1:
                return True
            elif sum in num_dict:
                return False
            else:
                n = sum

'''
通过分析该问题，利用一些分析结果，可以对算法进行优化。比如利用10以内的happy number只有1和7，
或者先求出100以内的所有happy number等。
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        happySet = set([1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97])

        while n>99:
            n = sum([int(x) * int(x) for x in list(str(n))])
        return n in happySet
    
    
    
 #方法三   辰星大佬
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hset = {n}
        while(n != 1):
            num = 0
            while n:
                n, remainder = divmod(n, 10) 
                num += remainder**2
            if num in hset: return False
            hset.add(num)
            n = num
        return True

   
