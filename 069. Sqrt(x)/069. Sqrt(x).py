'''
思路一
'''
class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r=x
        while r*r>x:
            r=(r+x/r)/2
        return r


#思路二
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        i=0
        j=x
        mid=0
        while True:
            mid=(i+j)/2
            if mid>x/mid:
                j=mid
            else:
                if (mid+1)>x/(mid+1):
                    return mid
                i=mid
