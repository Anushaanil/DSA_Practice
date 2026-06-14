class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_point=0
        sell_point=1
        profit=0

        while sell_point<len(prices):
            if prices[sell_point] < prices[buy_point]:
                buy_point=sell_point

            val = prices[sell_point] - prices[buy_point]
            profit = max(profit, val)
            sell_point+=1
            
        return profit