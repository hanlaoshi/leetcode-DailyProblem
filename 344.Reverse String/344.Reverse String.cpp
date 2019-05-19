#耗时64ms
#递归 逐个逆转
class Solution(object):
    def reverseString(s):
        if len(s) <=1:
            return s
        return self.reverseString(s[1:]) + s[0]
		
#耗时52ms
#前后对称位互换
class Solution(object):
    def reverseString(s):
        li = list(s)
        l = len(s)
        for i, j in zip(range(len(l)-1, 0, -1), range(l//2)):
             li[i], li[j] = li[j], li[i]
        reurn ''.join(li)

#耗时52ms		
#循环逆序
class Solution(object):
    def reverseString(s):
        return ''.join([s[i] for i in range(len(s)-1,-1,-1)])