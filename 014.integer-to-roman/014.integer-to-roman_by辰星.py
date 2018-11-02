#欢迎关注微信公众号：AI数据分析算法
#来自群成员 @辰星 的方法
class Solution: 
    def intToRoman(self,num): 
    '''
    :type num:int
    :rtype:str n4
    '''
    rtn=''
    conv_tab=(1000,100,10,1)
    conv_value={1000:('','M','MM','MMM'),100:
    (",'C','CC','CCC','CD','D','DC',"DCC','DCCC','CM'),10:
    (",'X','XX','XXX','XL','L','LX','LXX','LXXX','XC'),1:
    (",'I','II','III','IV','V','VI','VII','VIII','IX')}
    for base in conv_tab: 
      cnt=num //base
      num=num % base 
      rtn+=conv_value[base][cnt]
      return rtn
      
