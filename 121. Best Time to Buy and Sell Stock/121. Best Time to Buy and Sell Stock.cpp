class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) {
            return 0;
        }
        int profit = 0;
        int buy = prices[0];
        for (int i = 0; i < prices.size(); i++) {
            //截至第i天，买入的最低价格：第i-1天的价格与第i天的价格的最小值
            buy = min(buy, prices[i]);
            //截至第i天，获得的最大利润：第i-1天的利润与在第i天卖出得到的最大利润
            profit = max(profit, prices[i] - buy);
        }
        return profit;
    }
};
