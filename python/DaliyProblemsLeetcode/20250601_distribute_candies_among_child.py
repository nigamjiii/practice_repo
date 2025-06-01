class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ch1_min = max(0, n - (2 * limit))
        ch1_max = min(n, limit)
        ans = 0

        for i in range(ch1_min, ch1_max + 1):
            rem_candies = n - i

            ch2_min = max(0, rem_candies - limit)
            ch2_max = min(rem_candies, limit)
            ans += ch2_max - ch2_min + 1

        return ans

link = 'https://leetcode.com/problems/distribute-candies-among-children/?envType=daily-question&envId=2025-06-01'