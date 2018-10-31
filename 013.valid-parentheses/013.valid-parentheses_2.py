解法二：

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        # 空字符串 ，即无括号，但是也是有效的
        if n == 0:
            return True
        # 字符串长度为奇数 ，不可能匹配
        if n % 2 != 0:
            return False
        #算是做了个一个弊 ，利用python的replace剔除成对的括号    
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        return s == ''

解法三

```
class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            #将左括号依次append进列表
            if char in ["(","{","["]:
                stack.append(char)
            elif not stack: #这里是排除只有右括号的情况，如：‘）’
                return False
            #这里是到右括号时依次pop出成对的括号
            elif (char == ")") and (stack[len(stack)-1]=="("):
                stack.pop()
            elif (char == "}") and (stack[len(stack)-1]=="{"):
                stack.pop()
            elif (char == "]") and (stack[len(stack)-1]=="["):
                stack.pop()
            else:
                return False
        return len(stack)==0 #有效的括号时，上述代码会pop出所有字符，即长度为0
```
