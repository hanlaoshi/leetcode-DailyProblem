class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s) == 0 : return 0
        words = s.split(" ")
        count = 0
        for i in words:
            if not i == '':
                count = len(i)
        return count