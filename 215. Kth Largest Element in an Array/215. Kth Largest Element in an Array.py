1，python的collections库：代码写起来很清爽，但是集合操作相对慢。

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.Counter(s)

        ans = -1
        for x,c in enumerate(s):
            if d[c] == 1:
                ans = x
                break

        return ans
2，数组计数

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1

        hash = [0]*26
        for i in s:
            hash[ord(i) - 97] += 1

        for i in s:
            if hash[ord(i) -97] == 1:
                return s.index(i)

        return -1