解法1
DFS - 利用判断当前子串是否可以由wordDict中的词汇组成
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        res = []
        self.dfs(s, wordDict, 0, '', res)
        return res

    def check(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)    # s[:i]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

    def dfs(self, s, wordDict, i, temp, res):
        if i == len(s):
            res.append(temp[:-1])
        if self.check(s[i:], wordDict):
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    self.dfs(s, wordDict, j, temp + s[i:j] + ' ', res) 
（改进-法1）
dp已经统计了截止当前位置的字符串是否可以由wordDict中的词汇组成。
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        dp = self.check(s, wordDict)
        res = []
        self.dfs(s, wordDict, dp, '', res)
        return res

    def check(self, s, wordDict):
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp

    def dfs(self, s, wordDict, dp, temp, res):
        if not s:
            res.append(temp[:-1])
        for i in range(len(s)):
            if dp[i] and s[i:] in wordDict:
                self.dfs(s[:i], wordDict, dp, s[i:] + ' ' + temp, res)
