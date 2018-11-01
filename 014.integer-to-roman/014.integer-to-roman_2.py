#欢迎关注微信公众号：AI数据分析算法

#leetcode官网上60ms版本

UNITS = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
TENS = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
HUNDREDS = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
THOUSANDS = ['', 'M', 'MM', 'MMM', 'M(V)', '(V)', '(V)M', '(V)MM', '(V)MMM', 'M(X)']

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        return THOUSANDS[num // 1000] + HUNDREDS[(num // 100) % 10] + TENS[(num // 10) % 10] + UNITS[num % 10]
        
        
'''
class Solution:
    def intToRoman(self, num):
    	M = ["", "M", "MM", "MMM"];
    	C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
    	X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
    	I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
      return M[num//1000]+C[(num%1000)//100]+X[(num%100)//10]+I[num%10]
      
'''
