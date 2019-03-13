class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = i - 1; j >= 0 && !dp[i]; j--) {
                String check = s.substring(j, i);
                dp[i] = dp[j] && wordDict.contains(check);
            }
        }
        return dp[s.length()];   
    }
}