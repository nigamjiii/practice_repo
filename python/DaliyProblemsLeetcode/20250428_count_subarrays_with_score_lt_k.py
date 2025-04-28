from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        count = 0
        curr_sum = 0

        while r < n:
            curr_sum += nums[r]
            score = curr_sum * (r - l + 1)

            while score >= k and l <= r:
                curr_sum -= nums[l]
                l += 1
                score = curr_sum * (r - l + 1)

            count += r - l + 1
            r += 1

        return count

link = 'https://leetcode.com/problems/count-subarrays-with-score-less-than-k/?envType=daily-question&envId=2025-04-28'