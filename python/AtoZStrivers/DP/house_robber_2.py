from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob(nums) -> int:
            n = len(nums)
            prev2 = 0
            prev1 = nums[0]

            for i in range(2, n + 1):
                curr = max(prev2 + nums[i - 1], prev1)
                prev2 = prev1
                prev1 = curr

            return prev1

        return max(rob(nums[1:]), rob(nums[: n - 1]))
