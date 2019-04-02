#------------------------------第一种------------------------------------
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result, carry, val = "", 0, 0
        for i in xrange(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = val / 2, val % 2
            result += str(val)
        if carry:
            result += str(carry)
        return result[::-1]
#------------------------------第二种------------------------------------
class Solution:
     def addBinary(self, a, b):
         if len(a)==0: return b
         if len(b)==0: return a
         if a[-1] == '1' and b[-1] == '1':
             return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
         if a[-1] == '0' and b[-1] == '0':
             return self.addBinary(a[0:-1],b[0:-1])+'0'
         else:
             return self.addBinary(a[0:-1],b[0:-1])+'1'　
#----------------------------第三种---------------------------------------
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            su = carry
            if i >= 0:
                su += int(a[i])
            if j >= 0:
                su += int(b[j]) 
            carry = su / 2
            res += str(su % 2)
            i -= 1
            j -= 1
  
        if carry > 0:
            res += str(carry)
  
        return res[::-1] 　　