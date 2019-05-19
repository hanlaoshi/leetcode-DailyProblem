# 转载自 https://blog.csdn.net/coder_orz/article/details/51304295  
给定字符串，判断该字符串是否是“回文”。只考虑字母和数字，并忽略字母大小写。 
注：空字符串也是回文

思路方法
思路一
很直观的想法：将所有字母都转成小写，过滤掉原字符串里的其他字符得到新字符串；再按照“回文”的定义，判断处理后的字符串正序反序是否一致。

代码
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        new_s = [] #这里如果以字符串保存会超时，只好使用数组
        for c in s:
            #if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c >= '0' and c <= '9':
            if c.isalnum():
                new_s.append(c.lower())

        length = len(new_s)
        for i in range(0, length/2):
            if new_s[i] != new_s[length-i-1]:
                return False
        return True
注意 
本来我将 new_s 定义为 new_s = '' ，以字符串方式更新 new_s += c 结果超时(Time Limit Exceeded)了。一番搜索，发现别人也遇到过类似问题，用数组来定义 new_s = [] 就可以AC了。这应该跟 Python 内部处理字符串 + 的低效有关系。

思路二
双指针法，与思路一类似，不过不用生成新的字符串。
代码

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = -1
        j = len(s)
        while True:
            i += 1
            j -= 1
            if i > j:
                return True
            while i < j:
                if not s[i].isalnum():
                    i += 1
                else:
                    break
            while i < j:
                if not s[j].isalnum():
                    j -= 1
                else:
                    break
            if s[i].lower() != s[j].lower():
                return False

思路三
利用Python对List的强大的处理能力，可以写出更简洁高效的代码。

代码

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cleanlist = [c for c in s.lower() if c.isalnum()]
        return cleanlist == cleanlist[::-1]
