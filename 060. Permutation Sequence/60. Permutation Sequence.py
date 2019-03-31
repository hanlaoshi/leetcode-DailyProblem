class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        #0的阶乘一直到9!
        #因为题目说了n<=9
        self.fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        #找到对应的n应该对应的fac坐标,就是在第一项确定的情况一下，有(n-1)!种组合
        i = n - 1
        #构建序列，这个num是用来储存我们当前可以添加的数的，也是为避免重复
        num = list(range(1, n+1))
        ret = ""
        while i >= 0:
            #a用来获得我们要求的那一位在num里的下标
            a, b = k // self.fac[i], k % self.fac[i]
            #如果刚好整除干净，证明还在上一层
            if b == 0:
                a -= 1
            
            
            if a >= 0:
                ret += str(num[a])
                del num[a]
                i -= 1
            k = b
            #如果刚好整除完，则我们已经可以知道接下来的排序情况了，它一定是最大的
            #所以把剩下的可选的数字reverse来制造这种效果
            if b == 0:
                for i in reversed(num):
                    ret += str(i)
                break
        return ret
