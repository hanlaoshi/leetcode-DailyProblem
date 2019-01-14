'''
如果只有Integer、+和D的话这题就非常简单了，只用保存上两轮的得分，以及一个累加和就好了。但注意到这里有C可以撤销上一轮的得分，
并且C出现的次数没有限制，那么这里就必须用到栈来记录和管理之前每轮的得分了。

那么这题实际上就是对栈的操作了：

Integer：本轮得分为Integer，入栈。
+：本轮得分为当前两个栈顶值之和，入栈。
D：本轮得分为当前栈顶值的两倍，入栈。
C：栈顶出栈。
最终结果为当前栈中所有值的和。
'''

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        history = []
        for op in ops:
            if op == '+':
                history.append(history[-1] + history[-2])
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == 'C':
                history.pop()
            else:
                history.append(int(op))
        return sum(history)
