'''
递归生成码表

这种方法基于格雷码是反射码的事实，利用递归的如下规则来构造：

1位格雷码有两个码字
(n+1)位格雷码中的前2n个码字等于n位格雷码的码字，按顺序书写，加前缀0
(n+1)位格雷码中的后2n个码字等于n位格雷码的码字，按逆序书写，加前缀1
n+1位格雷码的集合 = n位格雷码集合(顺序)加前缀0 + n位格雷码集合(逆序)加前缀1
简言之就是递归。第（n+1）位的格雷码序列=（‘0’+第n位的正序） + （‘1’+第n位的逆序）

题目中说了n是非负数，当n=0的时候，返回[0]即可

'''

#方法一：循环版本
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        grays = dict()
        grays[0] = ['0']
        grays[1] = ['0', '1']
        for i in range(2, n + 1):
            n_gray = []
            for pre in grays[i - 1]:
                n_gray.append('0' + pre)
            for pre in grays[i - 1][::-1]:
                n_gray.append('1' + pre)
            grays[i] = n_gray
        return map(lambda x: int(x, 2), grays[n])

    #方法二：递推版本
    class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return map(lambda x: int(x, 2), self.bit_gray(n))
    
    def bit_gray(self, n):
        ans = None
        if n == 0:
            ans = ['0']
        elif n == 1:
            ans = ['0', '1']
        else:
            pre_gray = self.bit_gray(n - 1)
            ans = ['0' + x for x in pre_gray] + ['1' + x for x in pre_gray[::-1]]
        return ans
