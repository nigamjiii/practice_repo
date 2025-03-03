from typing import List

# Brute-Force: T.C -> O(n) and S.C -> O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        if n == 0:
            return 0

        candy = [1] * n

        for i in range(1, n):
            candy[i] = candy[i - 1] + 1 if ratings[i - 1] < ratings[i] else 1

        for i in range(n - 2, -1, -1):
            candy[i] = (
                max(candy[i], candy[i + 1] + 1)
                if ratings[i + 1] < ratings[i]
                else candy[i]
            )

        return sum(candy)

link = 'https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150'