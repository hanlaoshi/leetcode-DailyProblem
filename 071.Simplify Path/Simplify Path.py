# 题目大意

# 简化linux路径。

# 解题方法

# 看到这种来来回回，增增删删的题，一般都想到用栈。

# 我们把字符串按照/分割之后就得到了每个文件的目录，然后判断路径是添加还是向上层进行返回。这个题很简单了。


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = list()
        dirs = path.split('/')
        for dir in dirs:
            if not dir or dir == '.':
                continue
            if dir == '..':
                if stack:
                    stack.pop()
            else:                
                stack.append(dir)
        return '/' + '/'.join(stack)
