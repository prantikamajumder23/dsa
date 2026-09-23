class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0

        for price in prices:
            if price < buy:
                buy = price
            else:
                profit = max(profit, price - buy)

        return profit
       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna