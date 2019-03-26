花花酱 ： http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-730-count-different-palindromic-subsequences/

class Solution:
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        def count(S, i, j):
            if i > j: return 0
            if i == j: return 1
            if self.m_[i][j]:
                return self.m_[i][j]
            if S[i] == S[j]:
                ans = count(S, i + 1, j - 1) * 2
                l = i + 1
                r = j - 1
                while l <= r and S[l] != S[i]: l += 1
                while l <= r and S[r] != S[i]: r -= 1
                if l > r: ans += 2
                elif l == r: ans += 1
                else: ans -= count(S, l + 1, r - 1)
            else:
                ans = count(S, i + 1, j) + count(S, i, j - 1) - count(S, i + 1, j - 1)
            
            self.m_[i][j] = ans % (10 ** 9 + 7)
            return self.m_[i][j]
        
        n = len(S)
        self.m_ = [[None for _ in range(n)] for _ in range(n)]
        return count(S, 0, n - 1)
