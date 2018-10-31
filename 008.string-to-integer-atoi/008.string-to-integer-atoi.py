#方法2（python版本）执行用时： 44 ms  战胜90%提交记录

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 导入正则模块
        import re
        # 字符串中查找全部符合条件的整数，返回的是列表，第一个参数是正则，第二个参数是字符串
        # strip()字符串去空格
        ret = re.findall(r"^[-+]?\d+", str.strip())
        # 判断是否有匹配的值，没有的话返回0，例如"word values 987"，匹配不到，返回0
        if ret:
            ret_str = ret[0]  # 匹配的数字的字符串
            ret_str2 = ""  # 记录去符号的字符串，ret_str后面还要使用，所以定义一个新的变量记录
            # 判断是否带有符号 + or -
            if ret_str[0] == "-" or ret_str[0] == "+":
                ret_str2 = ret_str[1:]
            else:
                ret_str2 = ret_str
            # str转int
            ret_int = int(ret_str2)
            # 判断第一个字符是否为负号
            if ret_str[0] == "-":
                # 三目运算符，判断是否溢出
                # 如果ret_int <= 2**31则返回-ret_int，否则返回-2**31
                return -ret_int if ret_int <= 2**31 else -2**31
            else:
                return ret_int if ret_int < 2**31 else 2**31-1
        else:
            return 0
