from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n
        # Sn = n(n+1)/2
        Sn = (N * (N + 1)) // 2

        # Sn2 = n(n+1)(2n+1)/6
        Sn2 = (N * (N + 1) * (2 * N + 1)) // 6

        S = 0
        S2 = 0

        for i in range(n):
            for j in range(n):
                S += grid[i][j]
                S2 += grid[i][j] * grid[i][j]

        # x - y = S - Sn , x2 - y2 = S2 - Sn2
        val1 = S - Sn  # x - y
        val2 = S2 - Sn2
        val2 = val2 // val1  # x + y
        x = (val1 + val2) // 2
        y = x - val1

        return [x, y]


link = 'https://leetcode.com/problems/find-missing-and-repeated-values/'