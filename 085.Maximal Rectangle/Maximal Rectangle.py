#------------------辰星出品-----------------------
# encoding: utf-8
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        h, w = len(matrix) + 1, len(matrix[0]) + 1
        dp = [[0] * w for _ in range(h)]
        area = 0
        for i in range(1, h):
            cnt = 0
            for j in range(1, w):
                if matrix[i-1][j-1] == '1':
                    cnt += 1
                    dp[i][j] = cur_w = cnt
                    for h in range(i):                        
                        if dp[i-h][j] == 0: break
                        cur_w = min(cur_w, dp[i-h][j])
                        cur_area = cur_w * (h + 1)
                        if cur_area > area: area = cur_area
                else:                    
                    cnt = 0
                    dp[i][j] = 0
        return area

if __name__ == "__main__":  
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    print(Solution().maximalRectangle(matrix))
#===================第二种===========================
#思路：遍历每一行，在垂直放下进行相加，变成一维数组，利用84题的解法进行求解最大值class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        h = [0] * (m+1)
        self.ans = 0
        
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0
            self.ans = self.robot(self.ans,h)
        return self.ans
    
    def robot(self,maxL,h):
        stk = []
        m = len(h) - 1
        i = 0
        while i <= m:
            if len(stk) == 0 or h[stk[-1]] < h[i]:
                stk.append(i)
                i += 1
            else:
                now_idx = stk.pop()
                if len(stk) == 0:
                    maxL = max(maxL,i * h[now_idx])
                else:
                    maxL = max(maxL,(i - stk[-1] - 1) * h[now_idx])
        return maxL
