def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 判断匹配规则是否为空
        if p == "":
            # p为空的时候，判断s是否为空，则知道返回True 或 False
            return s == ""
        # 判断匹配规则是否只有一个
        if len(p) == 1:
            # 判断匹配字符串长度是否为1，和两者的第一个元素是否相同，或匹配规则使用.
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')
        # 匹配规则的第二个字符串不为*，当匹配字符串不为空的时候
        # 返回 两者的第一个元素是否相同，或匹配规则使用. and 递归新的字符串(去掉第一个字符的匹配字符串 和 去掉第一个字符的匹配规则)
        if p[1] != "*":
            if s == "":
                return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        # 当匹配字符串不为空 and (两者的第一个元素是否相同 or 匹配规则使用.)
        while s and (s[0] == p[0] or p[0] == '.'):
            # 到了while循环，说明p[1]为*，所以递归调用匹配s和p[2:](*号之后的匹配规则)
            # 用于跳出函数，当s循环到和*不匹配的时候，则开始去匹配p[2:]之后的规则
            if self.isMatch(s, p[2:]):
                return True
            # 当匹配字符串和匹配规则*都能匹配的时候，去掉第一个字符成为新的匹配字符串，循环
            s = s[1:]
        # 假如第一个字符和匹配规则不匹配，则去判断之后的是否匹配
        return self.isMatch(s, p[2:])
