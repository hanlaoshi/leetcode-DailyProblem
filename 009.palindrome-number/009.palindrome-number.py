class Solution:
    def isPalindrome(self,x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        n = x;
        temp = 0;
        while x!=0:
            temp = temp * 10 + x%10;
            x=x//10;        
        return n==temp
