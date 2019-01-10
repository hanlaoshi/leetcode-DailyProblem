class Solution {
public:
    int largestRectangleArea(int* height, int length) {
        stack<int> stk;
        int i = 0;
        int maxArea = 0;
        while(i < length){
            if(stk.empty() || height[stk.top()] <= height[i]){
                stk.push(i++);
            }else {
                int t = stk.top();
          stk.pop();
        int area = height[t] * (stk.empty() ? i : i - stk.top() - 1);
                maxArea = maxArea > area ? maxArea : area;
            }
        }
        return maxArea;
    }
 
int maximalRectangle(vector<vector<char> > &matrix) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int m = matrix.size();
        if(m == 0)return 0;
    int n = matrix[0].size();
        if(n == 0)return 0;
 
    int** dp = new int*[m];
    for(int i = 0; i < m; ++i){
      dp[i] = new int[n+1];
      memset(dp[i], 0, sizeof(int)*(n+1));
    }
    
 
    for(int j = 0; j < n; ++j)
      if(matrix[0][j] == '1')dp[0][j] = 1;
 
    for(int j = 0; j < n; ++j)
      for(int i = 1; i < m; ++i)
        if(matrix[i][j] == '1') dp[i][j] = dp[i-1][j] + 1;
 
    int maxarea = 0;
    for(int i = 0; i < m; ++i){
      int tmp = largestRectangleArea(dp[i],n+1);
      if(tmp > maxarea)
        maxarea = tmp;
    }
 
    for(int i = 0; i < m; ++i)
      delete[] dp[i];
    delete[] dp;
 
    return maxarea;
    }
};
