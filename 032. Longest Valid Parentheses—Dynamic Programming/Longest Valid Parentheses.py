'''
思路：1.使用栈进行操作
如果是左括号，直接入stack，
如果右括号，如果stack里没有元素匹对，说明有效括号已经结束，更新起始位置，有元素匹对pop出一个左括号匹对，
如果此时没了，不能保证不继续有效括号，所以根据当前的最长距离去更新maxlen，
如果此时还有 则计算与栈顶的索引相减来计算长度。

'''
        
class Solution:
    def longestValidParentheses(self, s):
        ans = 0
        n = len(s)
        stack = []
        st = 0
        for i in range(n):
            
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    st = i+ 1
                    continue
                else:
                    stack.pop()
                    if len(stack) == 0:
                        ans = max(ans,i - st + 1)
                    else:
                        ans = max(ans,i-stack[-1])
        return ans
