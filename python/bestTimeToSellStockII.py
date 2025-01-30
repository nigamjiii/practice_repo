from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)

        i = 0

        while i < n - 1:
            if prices[i] < prices[i+1]:
                profit += (prices[i+1] - prices[i])

            i +=1

        return profit 
    
link = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150'