
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for __ in range(1, n):
            result = self.getNext(result)
        return result

    def getNext(self, s):
        result = []
        start = 0
        while start < len(s):
            curr = start + 1
            while curr < len(s) and s[start] == s[curr]:
                curr += 1
            result.extend((str(curr - start), s[start]))
            start = curr
        return "".join(result)


if __name__ == "__main__":
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(5) == "111221"
