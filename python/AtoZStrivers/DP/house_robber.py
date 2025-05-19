from typing import List

# Memoization solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def rec(ind):
            if ind == 0:
                return nums[ind]

            if ind < 0:
                return 0

            if ind in memo:
                return memo[ind]

            pick = nums[ind] + rec(ind - 2)
            not_pick = rec(ind - 1)

            memo[ind] = max(pick, not_pick)
            return memo[ind]

        return rec(n - 1)
  
# Tabulation solution  
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("-inf")] * (n + 1)

        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return dp[n]
 
# Space Optimization in Tabulation   
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = 0
        prev1 = nums[0]

        for i in range(2, n + 1):
            curr = max(prev2 + nums[i - 1], prev1)
            prev2 = prev1
            prev1 = curr

        return prev1
    
link = 'https://leetcode.com/problems/house-robber/'


