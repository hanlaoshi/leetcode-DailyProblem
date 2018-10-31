class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        length = 0
        char_set = set()
        start = end = 0
        while start < len(s) and end < len(s):
            if s[end] in char_set:
                length = max(length, end - start)
                char_set.remove(s[start])
                start += 1
            else:
                char_set.add(s[end])
                end += 1
        return max(length, end - start)
        
        



'''
#采用字典
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        start = len_max = 0
        char_dict = {}
        for i in range(len(s)):
            if s[i] in char_dict and start <= char_dict[s[i]]:
                start = char_dict[s[i]] + 1
            else:
                len_max = max(len_max, i - start + 1)
            char_dict[s[i]] = i
        return len_max

#使用enumerate和Python字典的get方法
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        max_length, start, char_dict = 0, 0, {}
        for idx, char in enumerate(s, 1):
            if char_dict.get(char, -1) >= start:
                start = char_dict[char]
            char_dict[char] = idx
            max_length = max(max_length, idx - start)
        return max_length


'''
