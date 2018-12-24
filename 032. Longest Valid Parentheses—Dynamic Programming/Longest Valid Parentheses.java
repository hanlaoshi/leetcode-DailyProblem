class Solution {
    public int longestValidParentheses(String s) {
        if (s == null || s.length() < 2) {
            return 0;
        }
        
        int[] dp = new int[s.length()];
        int max = 0;
        dp[0] = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                continue;
            }
            int i1 = i - dp[i - 1] - 1;
             if (i1 < 0) {
                continue;
            }
            if (s.charAt(i1) == '(') {
                int pre = i1 - 1 < 0 ? 0 : i1 - 1;
                dp[i] = dp[i - 1] + 2 + dp[pre];
            }
            max = Math.max(dp[i], max);
        }

        return max;
    }
}