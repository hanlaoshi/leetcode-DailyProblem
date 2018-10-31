class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_length = len(s)
        ans = ""
        if numRows <= 1:
            return s
        for i in range(numRows):
            c1 = 2*numRows - 2*(i+1)
            c2 = 2 * i
            cnt = i

            ans += s[cnt]
            while cnt < str_length:
                if c1 != 0:
                    cnt += c1
                    if cnt < str_length:
                        ans += s[cnt]
                if c2 != 0:
                    cnt += c2
                    if cnt < str_length:
                        ans += s[cnt]

        return ans
