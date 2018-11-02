#欢迎关注微信公众号：AI数据分析算法
#本体解法来源于群内成员@李振兴
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
        def intToRoman(self,num):
            ret = ""
            A = map(int,str(num))[::-1]
            indexi = 0
            for i in A:
              ret - r[i][indexi] + ret
              indexi +=1
            return ret
            
        
