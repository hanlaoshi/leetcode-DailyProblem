'''
根据罗马数字的规则，只有在前面的字母比当前字母小的情况下要执行减法，
其他情况只需要把罗马字母对应的数字直接相加即可。
如果发现前一个字母比当前字母小，就减去前一个字母，
因为错误的把它加入了结果，且在加上当前字母时还要减去前一个字母的值。

'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = 0
        for i in range(len(s)):
            if i > 0 and map[s[i]] > map[s[i - 1]]:
                result -= map[s[i - 1]]
                result += map[s[i]] - map[s[i - 1]]
            else:
                result += map[s[i]]
        return result


if __name__ == "__main__":
    So = Solution()
    print(So.romanToInt("XII"))
    print(So().romanToInt("XXI")) 
    print(So().romanToInt("XCIX")) 
