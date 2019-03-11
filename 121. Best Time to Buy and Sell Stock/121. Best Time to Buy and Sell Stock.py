class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit = 0
        minimum = prices[0]
        for i in prices:
            minimum = min(i, minimum)
            profit = max(i - minimum, profit)
        return profit