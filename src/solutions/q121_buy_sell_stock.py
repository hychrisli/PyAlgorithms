from src.base.solution import Solution
from src.tests.q121_test_buy_sell_stock import BuySellStockTestCases
import math


"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/description

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.


"""

class BuySellStock(Solution):
    def run_test(self, input):
        return self.maxProfit(input)

    def print_output(self, output):
        print(output)

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return BuySellStockTestCases()

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if not prices: return max_profit

        minp =prices[0]

        for p in prices[1:]:
            minp = min(minp, p)
            max_profit = max(max_profit, p - minp)

        return max_profit


if __name__ == '__main__':
    sol = BuySellStock()
    sol.run_tests()