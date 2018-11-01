#欢迎关注微信公众号：AI数据分析算法

#此种方法在leetcode上测试运行时间72ms
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strings = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ''
        for i in range(len(nums)):
            while num >= nums[i]:
                num -= nums[i]
                result += strings[i]
        return result


if __name__ == "__main__":
    print(Solution().intToRoman(2)) 
    print(Solution().intToRoman(21)) 
    print(Solution().intToRoman(99))
    
    
    
    '''
    #leetcode上同样一个72ms的版本
    class Solution(object):
    
    r = {
        # value is an array of strings for each key in
        # the ones, tens, hundreds, and thousands places
        # up to 3000 (since given max is 3999)
        1: ['I', 'X', 'C', 'M'],
        2: ['II', 'XX', 'CC', 'MM'],
        3: ['III', 'XXX', 'CCC', 'MMM'],
        4: ['IV', 'XL', 'CD'],
        5: ['V', 'L', 'D'],
        6: ['VI', 'LX', 'DC'],
        7: ['VII', 'LXX', 'DCC'],
        8: ['VIII', 'LXXX', 'DCCC'],
        9: ['IX', 'XC', 'CM']
    }
        
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ""
        for i in range(len(str(num))):
            digit = (num // (10 ** i)) % 10
            if digit > 0:
                ret = self.r[digit][i] + ret
        return ret
    
    '''
