# Recursion Solution, will give TLE because T.C = O(2^n)
class Solution:
    def climbStairs(self, n: int) -> int:

        def rec(n):
            if n == 0:
                return 1

            if n < 0:
                return 0

            return rec(n - 1) + rec(n - 2)

        return rec(n)
 
# Memoization Solution, T.C = O(n) and S.C = O(n)   
class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n + 1)

        def rec(n, dp):
            if n == 0:
                return 1

            if n < 0:
                return 0

            if dp[n] != -1:
                return dp[n]

            dp[n] = rec(n - 1, dp) + rec(n - 2, dp)
            return dp[n]

        return rec(n, dp)
    
# Tabulation(bottom-up) Solution, T.C = O(n) and S.C = O(n) 
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i - 2 >= 0:
                dp[i] += dp[i - 2]

        return dp[n]
    
# Space Optimization with tabulation , T.C = O(n) S.C = O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prev2 = 0

        for i in range(1, n + 1):
            curr = prev + prev2
            prev2 = prev
            prev = curr

        return prev


link = 'https://leetcode.com/problems/climbing-stairs/'
