from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        s = 0
        minPrice = float('inf')

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                s = max(s, prices[i] - minPrice)

        return s
        