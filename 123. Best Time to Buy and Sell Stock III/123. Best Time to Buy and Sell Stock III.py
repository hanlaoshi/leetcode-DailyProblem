有了前面两个问题的基础，我们首先想通过贪心解决这个问题。但是这个问题不行，因为有最多两比交易的限制。但是正因为如此这个问题也变得非常容易，我们可以参考第一个问题的解决思路。
我们主要有这样几种状态buy1、buy2、sell1和sell2，涉及的状态方程为

buy1=max(buy1,−prices[i]) 

sell1=max(sell1,buy1+prices[i]) 

buy2=max(buy2,sell1−prices[i]) 

sell2=max(sell2,buy2+prices[i]) 

然后就是考虑边界问题，
很显然buy1[0]=-prices[0]，而sell1=0（相当于买入后再卖出）、buy2-prices[0]（相当于买入后再卖出再买入）、sell2=0（相当于买入后再卖出再买入再卖出）。
最后我们只要考虑max(sell1, sell2)，也就是卖一次的收益大，还是卖两次的收益大。最后代码就是

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        len_prices = len(prices)
        buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0

        for i in range(1, len_prices):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return max(sell1, sell2)
