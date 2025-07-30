# Problem: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Tags: Array, Greedy
# Approach: Greedy (Track min price and max profit)
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')    # track the lowest price seen so far
        max_profit = 0              # track the maximum profit found so far

      # loop through each day's price
        for price in prices:
            if price < min_price:
                min_price = price   # update min_price if current price is lower
            elif price - min_price > max_profit:
                max_profit = price - min_price  # update max_profit if current profit is higher

        return max_profit    # return the highest profit achievable

  
