class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i , j = 0 , n - 1
        profit = 0
        min = prices[0]
        for i in range(n):
            temp = prices[i] - min
            profit = max(temp, profit)
            if prices[i] < min:
                min = prices[i]
        return profit

