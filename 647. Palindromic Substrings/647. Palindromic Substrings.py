class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        p = [0]*n
        id = mx = res = 0
        for i in range(1,n-1):
            if(mx > i):
                p[i] = min(mx-i, p[2*id-i])
            while i+p[i]+1 < n and i-p[i]-1 >=0 and s[i+p[i]+1] == s[i-p[i]-1]:
                p[i] += 1
            if(i + p[i] > mx):
                id = i
                mx = i + p[i]
            res += (p[i]+1)/2
        return res